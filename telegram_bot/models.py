from tortoise.models import Model
from tortoise import fields


class User(Model):
    user_id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    token = fields.CharField(max_length=500)
    tg_user_id = fields.IntField(max_length=50)

    class Meta:
        table = "users"

    def __str__(self):
        return f"[{self.user_id}] {self.full_name}"