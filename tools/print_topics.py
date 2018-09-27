from learning_logs.models import Topic


for topic in Topic.objects.all():
    print (topic, topic.owner)