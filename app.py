from flask import Flask, request, redirect, url_for

app = Flask(__name__)

DUMMY_OTP = "123456"

@app.route("/")
def login():
    return """
    <h2>Login Screen</h2>
    <form action="/send-otp" method="post">
        <label>Customer ID / Mobile Number:</label><br>
        <input type="text" name="userid" required><br><br>
        <button type="submit">Send OTP</button>
    </form>
    """

@app.route("/send-otp", methods=["POST"])
def send_otp():
    userid = request.form["userid"]
    return f"""
    <h2>OTP Screen</h2>
    <p>Dummy OTP sent to user: <b>{DUMMY_OTP}</b></p>
    <form action="/verify-otp" method="post">
        <input type="hidden" name="userid" value="{userid}">
        <label>Enter OTP:</label><br>
        <input type="text" name="otp" required><br><br>
        <button type="submit">Verify OTP</button>
    </form>
    """

@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    otp = request.form["otp"]

    if otp == DUMMY_OTP:
        return redirect(url_for("home"))
    else:
        return """
        <h2>Invalid OTP</h2>
        <a href="/">Try Again</a>
        """

@app.route("/home")
def home():
    return """
    <h2>Customer Details</h2>
    <form action="/appointment" method="post">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Email ID:</label><br>
        <input type="email" name="email" required><br><br>

        <label>Mobile Number:</label><br>
        <input type="text" name="mobile" required><br><br>

        <button type="submit">Proceed to Appointment Booking</button>
    </form>
    """

@app.route("/appointment", methods=["POST"])
def appointment():
    name = request.form["name"]
    email = request.form["email"]
    mobile = request.form["mobile"]

    return f"""
    <h2>Appointment Booking Screen</h2>
    <form action="/confirm" method="post">
        <input type="hidden" name="name" value="{name}">
        <input type="hidden" name="email" value="{email}">
        <input type="hidden" name="mobile" value="{mobile}">

        <label>Select Branch:</label><br>
        <select name="branch" required>
            <option>Hyderabad Branch</option>
            <option>Mumbai Branch</option>
            <option>Delhi Branch</option>
            <option>Bangalore Branch</option>
        </select><br><br>

        <label>Reason to Visit:</label><br>
        <select name="reason" required>
            <option>Account Opening</option>
            <option>Loan Enquiry</option>
            <option>KYC Update</option>
            <option>General Banking</option>
        </select><br><br>

        <label>Select Slot:</label><br>
        <select name="slot" required>
            <option>10:00 AM - 10:30 AM</option>
            <option>11:00 AM - 11:30 AM</option>
            <option>02:00 PM - 02:30 PM</option>
            <option>03:00 PM - 03:30 PM</option>
        </select><br><br>

        <button type="submit">Book Appointment</button>
    </form>
    """

@app.route("/confirm", methods=["POST"])
def confirm():
    name = request.form["name"]
    email = request.form["email"]
    mobile = request.form["mobile"]
    branch = request.form["branch"]
    reason = request.form["reason"]
    slot = request.form["slot"]

    return f"""
    <h2>Appointment Confirmed</h2>
    <p>Dear <b>{name}</b>, your appointment has been booked successfully.</p>

    <h3>Appointment Details</h3>
    <p><b>Email:</b> {email}</p>
    <p><b>Mobile:</b> {mobile}</p>
    <p><b>Branch:</b> {branch}</p>
    <p><b>Reason:</b> {reason}</p>
    <p><b>Slot:</b> {slot}</p>

    <hr>
    <h3>Dummy Email Sent</h3>
    <p>Appointment confirmation email sent to: <b>{email}</b></p>
    """

app.run(host="0.0.0.0", port=5000)