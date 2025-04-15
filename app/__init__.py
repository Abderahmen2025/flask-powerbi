
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "super-secret-key"

from app import views
