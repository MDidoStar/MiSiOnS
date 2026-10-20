import streamlit as st
from random import randint as ri
from time import sleep as sl
def wait(l,s):
    with st.spinner(l):
        sl(s)
def stud():
    st.header("AI Study Buddy")
    st.write("Welcome to AI Study Buddy!")
    st.divider()
    subjects = ["English", "Mathematics", "Science", "ICT"]
    eng = ["Set Helpful Targets", "Don't Be Afraid of Mistakes", "Study Little and Often", "Focus on Communication", "Stay Organized and Consistent"]
    math = ["Allow Plenty of Study Time", "Practice Past Questions", "Create a Consistent Study Routine", "Understand the 'Why' Behind the Math", "Use Active Learning Techniques"]
    sci = ["Active Recall", "Spaced Repetition", "Interleaving", "Mnemonic Devices", "Focused Study Sessions"]
    ict = ["Set Up a Study Schedule with Digital Calendars", "Use Educational Apps", "Use Note-Taking Apps", "Join Collaborative Study Groups", "Use Playlists to Help Focus"] # https://classtechtips.com/2023/11/20/study-tips/
    sub = st.selectbox("Choose a Subject", options=subjects)
    ta = st.text_area("Write The Note you need help with")
    b = st.button("Get Study Tip")
    if b:
        wait("Generating Tip", 3)

        if sub == "English":
            st.success(eng[ri(1, 5)])
        elif sub == "Mathematics":
            st.success(math[ri(1, 5)])
        elif sub == "ICT":
            st.success(ict[ri(1, 5)])
        else:
            st.success(sci[ri(1, 5)])
def gen_two():
        f = f"{ri(0,9)}"
        f = f"{f}{ri(0,9)}"
        return f
def last_two(l):
    f = f"{l[len(l) - 2]}{l[len(l) - 1]}"
    return f
def blaze():
    st.header("BlazeX Email Creator")
    st.write("Generate your work email in a flash with BlazeX Email Creator!")
    fn = st.text_input("Enter your first name", max_chars=12, icon='🧑') # max len = 12 ch
    ln = st.text_input("Enter your last name", max_chars=12, icon='🧓') # max len = 12 ch
    pn = st.text_input("Enter your phone number", max_chars=11, icon='📞') # max len = 11 ch
    dps = {
        "Technology 🏢":"dev",
        "Marketing 🏢":"mkt",
        "Operations 🏢":"op",
        "Finance 🏢":"fin",
        "Sales 🏢":"sl",
        "Human Resources 🏢":"hr"
        }
    dp = st.selectbox("Choose your department", options=list(dps.keys()))

    
    def make_email(first, last, phone, depart, departs):
        two_rand = gen_two()
        pnlt = last_two(phone)
        f = f"{first}.{last}.{departs[depart]}.{pnlt}.{two_rand}@BlazeX.com"
        return f

    if st.button("Make Email"):
        wait("Generating Email", 3)
        if pn.isdigit() and len(pn)  > 2 and pn and fn and ln:
            email = make_email(fn, ln, pn, dp, dps)
            data = {"First Name": fn, "Last Name": ln, "Phone Number": pn, "Department": dp}
            st.code(email)
            exp = st.expander("Your Information")
            exp.table(data)
        else:
            st.error("Please Enter All Your Correct Information")
def bonus(nid):
    first = nid[0] == "2" or nid[0] == "3"
    s = f"{nid[1]}{nid[2]}"
    sec = int(s) > -1 and int(s) < 100
    f = f"{nid[3]}{nid[4]}"
    four = int(f) > 0 and int(f) < 12
    si = f"{nid[5]}{nid[6]}"
    six = int(si) > 0 and int(si) < 32
    return first, sec, four, six
def is_id_valid(national_id):
    l = len(national_id) == 14
    n = national_id.isdigit()
    if n == False or l == False:
        fd, sd, fod, six = True, True, True, True
    else:
        fd, sd, fod, six = bonus(national_id)

    return l, n, fd, sd, fod, six
def booling(b, m, f):
    fin = f
    if b == False:
        st.warning(m)
        fin = False
    return fin
def niv():
    st.header("National ID Validator")
    st.write("Welcome to National ID Validator!")
    st.image("rules.png", caption="Important Rules for First Seven Digits")
    id = st.text_input("Enter 14-digit National ID:")
    b = st.button("Validate")
    if b:
        length_bool, digit_bool, first_digit, second_digit, fourth_digit, sixth_digit = is_id_valid(id)
        wait("Checking Validity", 3)
        f_bool = True
        nf_bool = booling(length_bool, "ID must be 14 digits long", f_bool)
        f_bool = nf_bool
        nf_bool = booling(digit_bool, "ID must contain digits only", f_bool)
        f_bool = nf_bool        
        nf_bool = booling(first_digit, "Invalid birth date in ID", f_bool)
        f_bool = nf_bool  
        nf_bool = booling(second_digit, "Invalid year in birth date in ID", f_bool)
        f_bool = nf_bool
        nf_bool = booling(fourth_digit, "Invalid month in birth date in ID", f_bool)
        f_bool = nf_bool
        nf_bool = booling(sixth_digit, "Invalid day in birth date in ID", f_bool)
        f_bool = nf_bool
        if f_bool == False:
            st.error("Incomplete: ID Invalid")
        else:
           st.success("Complete: ID Valid") 
