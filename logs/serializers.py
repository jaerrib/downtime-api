from rest_framework import serializers

from .models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "customer_name",
            "assembly_number",
            "part_number",
            "lot_number",
            "date",
            "shift",
            "down_time",
            "restart_time",
            "problem",
            "root_cause",
            "corrective_action",
            "impact",
            "initiator",
        )
        model = Log
