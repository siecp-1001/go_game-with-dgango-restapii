from django.db import models

class GameState(models.Model):
    board_state = models.JSONField(default=dict)  # Store the board as JSON
    next_color = models.CharField(max_length=5, choices=[('BLACK', 'Black'), ('WHITE', 'White')])
    winner = models.CharField(max_length=5, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
