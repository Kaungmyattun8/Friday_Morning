from flask import Flask, render_template, abort, request, redirect, flash, jsonify
from models import Book

app = Flask(__name__)
app.secret_key = "change-this-secret"  # needed for flash messages

@app.route("/")
@app.route("/books")
def book_list():
    q = request.args.get("q", "")
    if q:
        books = Book.search(q)
    else:
        books = Book.all()
    return render_template("books.html", books=books, q=q)

@app.route("/books/<int:id>")
def book_detail(id):
    book = Book.load(id)
    if book is None:
        abort(404)
    return render_template("book.html", book=book)

@app.route("/books/add", methods=["GET", "POST"])
def book_add():
    if request.method == "POST":
        book = Book(request.form["title"],
                    request.form["author"],
                    request.form["year"])
        errors = book.validate()
        if errors:
            for e in errors:
                flash(e, "danger")
            return render_template("form.html", book=book, heading="Add a book")
        book.save()
        flash("Book added.", "success")
        return redirect("/books")
    empty = Book("", "", "")
    return render_template("form.html", book=empty, heading="Add a book")

@app.route("/books/<int:id>/edit", methods=["GET", "POST"])
def book_edit(id):
    book = Book.load(id)
    if book is None:
        abort(404)
    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.year = request.form["year"]
        errors = book.validate()
        if errors:
            for e in errors:
                flash(e, "danger")
            return render_template("form.html", book=book, heading="Edit a book")
        book.update()
        flash("Book updated.", "success")
        return redirect(f"/books/{id}")
    return render_template("form.html", book=book, heading="Edit a book")

@app.route("/books/<int:id>/delete", methods=["POST"])
def book_delete(id):
    book = Book.load(id)
    if book is None:
        abort(404)
    book.delete()
    flash("Book deleted.", "success")
    return redirect("/books")

@app.route("/api/books")
def api_books():
    return jsonify([b.to_dict() for b in Book.all()])

@app.route("/api/books/<int:id>", methods=["DELETE"])
def api_book_delete(id):
    book = Book.load(id)
    if book is None:
        return jsonify({"error": "not found"}), 404
    book.delete()
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)