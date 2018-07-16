from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
#from chatterbot.trainers import ListTrainer
#from chatterbot import ChatBot
# import os
# bot = ChatBot('Test')
#
# bot.set_trainer(ListTrainer)
#
# for _file in os.listdir('chat_files'):
#     chats = open('chat_files/' + _file, 'r').readlines()
#
#     bot.train(chats)
#
# while True:
#     request = input('You: ')
#     response = bot.get_response(request)
#
#     if response.confidence > 0.7:
#         print('Bot: ', response)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joshua'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}, ex={}'.format(
            form.username.data, form.remember_me.data, form.ex.data))
        return redirect('/index')
    return render_template('login.html', title='Sigdf n In', form=form)
