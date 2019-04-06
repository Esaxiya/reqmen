from flask import request
from flask import session
from flask import url_for
from flask import redirect
from flask import render_template
from config.models import User
from config.models import Question
from config.models import Comment
from config.exts import db


def question_service():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        print("提交问答成功、、、、")
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        # 获取当前登陆的用户的信息
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.user = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('content'))


def detail_service(question_id):
    question_detail = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question_detail=question_detail)


def add_comment_service():
    content = request.form.get('content')
    question_id = request.form.get('question_id')
    user_id = session['user_id']
    comment = Comment(content=content, user_id=user_id)
    user = User.query.filter(User.id == user_id).first()
    question = Question.query.filter(Question.id == question_id).first()
    comment.author = user
    comment.question = question
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


def content_show():
    contents = {'questions': Question.query.order_by('create_time').all(), }
    return render_template('content.html', **contents)