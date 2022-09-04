from flask import Blueprint, request, flash, redirect, url_for
from flask import render_template

from extensions import db
from apps.lottery.models import Lottery
from apps.lottery.forms import LotteryForm

lottery_blueprint = Blueprint(
    "lottery", __name__, template_folder="templates", url_prefix="/lottery"
)


@lottery_blueprint.route("/", methods=["GET"])
def index():
    lotteries = Lottery.query.all()

    return render_template("lottery/index.html", admin_page=True, lotteries=lotteries)


@lottery_blueprint.route("/create", methods=["GET"])
def create():
    form = LotteryForm()

    return render_template("lottery/create.html", admin_page=True, form=form)


@lottery_blueprint.route("/store", methods=["POST"])
def store():
    form = LotteryForm(request.form)

    if form.validate_on_submit():
        data = Lottery(
            name=form.name.data,
            description=form.description.data,
            max_participant=form.max_participant.data,
        )
        try:
            db.session.add(data)
            db.session.commit()

            flash("Data undian berhasil ditambahkan!", "success")

            return redirect(url_for("lottery.index"))
        except Exception as error:
            message = "Terjadi kesalahan saat mengola data!, error : %s" % error
    else:
        message = "Terjadi kesalahan pada data yang anda masukan!"

    flash(message, "danger")

    return redirect(url_for("lottery.create"))


@lottery_blueprint.route("/edit/<int:id>/edit", methods=["GET"])
def edit(id):
    lottery = Lottery.query.get(id)

    form = LotteryForm(obj=lottery)

    return render_template("lottery/edit.html", admin_page=True, form=form, id=id)


@lottery_blueprint.route("/edit/<int:id>/update", methods=["POST"])
def update(id):
    form = LotteryForm(request.form)

    if form.validate():
        try:
            lottery = Lottery.query.get(id)
            lottery.name = form.name.data
            lottery.max_participant = form.max_participant.data
            lottery.description = form.description.data

            db.session.commit()

            flash("Data undian %s berhasil diubah!" % lottery.name, "success")

            return redirect(url_for("lottery.index"))
        except Exception as error:
            message = "Terjadi kesalahan saat mengubah data!, error : %s" % error
    else:
        message = "Terjadi kesalahan pada data yang anda masukan!"

    flash(message, "danger")

    return redirect(url_for("lottery.edit", id=id))


@lottery_blueprint.route("/delete", methods=["POST"])
def delete():
    id = request.form["id"]
    lottery = Lottery.query.get(id)

    if lottery is not None:
        try:
            db.session.delete(lottery)
            db.session.commit()

            flash("Data undian %s berhasil dihapus!" % lottery.name, "success")
        except Exception as error:
            flash("Terjadi kesalahan saat menghapus data!, error : %s" % error)
    else:
        flash("Data undian tidak ditemukan !")

    return redirect(url_for("lottery.index"))


# Metode dalam routing
# Membuat function create()
# Membuat Form Data
# Membuat function store()
# Mengirim dan Menerima data form dari user -> request.form
# Fungsi redirect() & url_for()
# Membuat Form Data menggunakan WTForms
# Memisahkan Template generator untuk form dengan macro
# Memvalidasi data
# Menyimpan Data
# Menambahkan Pesan Sukses & Error
# Membuat Template untuk pesan error & sukses
# Menambahkan Exception
# Menampilkan Data Pada Index Lottery
# Membuat Tabel untuk tempat data
# Menambahkan Tombol Create
