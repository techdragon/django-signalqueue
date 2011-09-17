
from django import template
from signalqueue.worker import queues

register = template.Library()

@register.simple_tag
def queue_length(queue_name):
    if queue_name in queues:
        return queues[queue_name].count()
    return -1

@register.simple_tag
def queue_classname(queue_name):
    return str(queues[queue_name].__class__.__name__)

@register.simple_tag
def sock_status_url():
    import socket
    from django.conf import settings
    return "ws://%s:%s/sock/status" % (socket.gethostname().lower(), settings.SQ_WORKER_PORT)

@register.inclusion_tag('admin/sidebar_queue_module.html', takes_context=True)
def sidebar_queue_module(context):
    from signalqueue.utils import static
    qs = dict(queues.items())
    default = qs.pop('default')
    qjs = static('js/jquery.queuestatus.js')
    return dict(default=default, queues=qs, queue_javascript=qjs)



