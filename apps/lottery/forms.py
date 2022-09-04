from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, IntegerField


class LotteryForm(FlaskForm):
    name = StringField(
        "Nama Undian", [validators.Length(min=4, max=50), validators.DataRequired()]
    )
    description = TextAreaField(
        "Deskripsi Undian",
        [validators.Length(min=6, max=200), validators.DataRequired()],
    )
    max_participant = IntegerField("Maksimal Partisipan", [validators.DataRequired()])
