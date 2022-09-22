import uuid


class Email:
    uniqe_id = str(uuid.uuid4())
    generated_email = f"kazia{uniqe_id[:5]}@gmail.com"



