from app.services.redis_tasks import enqueue_email_to_redis
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from .forms import SendEmailForm

bp = Blueprint("dashboard", __name__)

@bp.route("/", methods=["GET", "POST"])
def home():
    form = SendEmailForm()
    if request.method == "POST" and form.validate(): 
        enqueue_email_to_redis(recipients=[form.email.data],subject=form.subject.data, html_body=form.body.data)
        flash("Email sent successfully!", "success")
        return redirect(url_for('dashboard.home'))
    else:
        print(request.method)
        return render_template(
            "dashboard/home.html", title="Home", form=form
        )

