from flask import render_template, current_app, request
from wlanpi_webui.speedtest import bp

@bp.route("/")
@bp.route("/speedtest")
def speedtest():
    spt_port = "8080"
    base = request.host.split(":")[0]
    iframe = f"http://{base}:{spt_port}/speedtest.html"
    return render_template(
        "/public/speedtest.html",
        wlanpi_version=current_app.config['WLANPI_VERSION'],
        webui_version=current_app.config['WEBUI_VERSION'],
        title="speedtest",
        iframe=iframe,
    )

@bp.route("/speedtest2")
def speedtest2():
    spt_port = "8080"
    base = request.host.split(":")[0]
    iframe = f"http://{base}:{spt_port}/wip/speedtest.html"
    return render_template(
        "/public/speedtest.html",
        wlanpi_version=current_app.config['WLANPI_VERSION'],
        webui_version=current_app.config['WEBUI_VERSION'],
        title="speedtest",
        iframe=iframe,
    )
