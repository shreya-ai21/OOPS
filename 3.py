email=input("Enter your email address:")

em_index=email.index('@')
if '@' in email and em_index!=0 and email[-1]!='@' and '.' in email[em_index+1::] and email[em_index+1].isalnum() and email[-1]!='.' and email[0].isalnum() and len(email)<=256:
    print("True")
else:
    print("False")
    