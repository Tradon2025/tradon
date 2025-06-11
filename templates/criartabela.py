@app.route("/status_reds")
def status_reds():
    if "usuario_id" not in session:
        return redirect("/login")

    usuario_id = session["usuario_id"]
    reds_por_metodo = contar_reds_seguidos_por_metodo(usuario_id)
    print("REDS:", reds_por_metodo)
    return render_template("status_reds.html", reds=reds_por_metodo)