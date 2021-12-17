from kanpai import Kanpai

register = Kanpai.Object({

    "id": Kanpai.Number(),
    "first_name": Kanpai.String().trim().required("first_name_required").match(
        pattern="^[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z ]+[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z-_ ]*$",
        error="name_letters_only").min(3,
                                       error="character_allowed_3to25").max(
        25,
        error="character_allowed_3to25"),

    "last_name": Kanpai.String().trim().match(
        pattern="^[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z ]+[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z-_ ]*$",
        error="name_letters_only").min(1,
                                       error="character_allowed_1to25").max(
        25,
        error="character_allowed_1to25"),

    "age": Kanpai.Number().min(18, error="age_not_valid"),

    "mail_id": Kanpai.Email(error="email_not_valid").trim(),

})
