def is_valid_email(email:str):
    if '@' in email:
        em_index=email.index('@')
        if em_index!=0 and email[-1]!='@' and '.' in email[em_index+1::] and email[em_index+1].isalnum() and email[-1]!='.' and email[0].isalnum() and len(email)<=256:
            print("True")
        else:
            print("False")
    else:
        print("False")

email=input("Enter your email address:")
is_valid_email(email)

    