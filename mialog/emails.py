"""
用来存储发送电子邮件的函数
"""
from threading import Thread

from flask import url_for, current_app
from flask_mail import Message

from mialog.extensions import mail


def _send_async_mail(app, message):
    with app.app_context():
        mail.send(message)


def send_mail(subject, to, html):
    app = current_app._get_current_object()
    message = Message(subject, reply_to=[to], html=html)
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()
    return thr


def send_new_comment_email(post):
    post_url = url_for('blog.show_post', post_id=post.id, _external=True) + "#comments"
    send_mail(subject='新的评论', to=current_app.config['BLUELOG_EMAIL'],
              html='<p>收到一条新的评论<i>{}</i>, 点击链接查看详情:</p>'
                   '<p><a href="{}">{}</a></P>'
                   '<p><small style="color: #868e96">此邮件无需回复.</small></p>'
                   .format(post.title, post_url, post_url))


def send_new_reply_email(comment):
    post_url = url_for('blog.show_post', post_id=comment.post_id, _external=True) + '#comments'
    send_mail(subject='新的回复', to=comment.email,
              html='<p>你评论的文章<i>{}</i>收到了回复, 点击链接查看详情: </p>'
                   '<p><a href="{}">{}</a></p>'
                   '<p><small style="color: #868e96">此邮件无需回复.</small></p>'
                   .format(comment.post.title, post_url, post_url))




