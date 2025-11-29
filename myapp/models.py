from django.db import models


class Analysis(models.Model):
    """Stores simple water analysis values for common ions.

    Fields are float values (use appropriate units in your UI, e.g. mg/L).
    """
    id = models.AutoField(primary_key=True)
    ca = models.FloatField("Ca", default=0.0, help_text="Calcium value")
    mg = models.FloatField("Mg", default=0.0, help_text="Magnesium value")
    na = models.FloatField("Na", default=0.0, help_text="Sodium value")
    so4 = models.FloatField("SO4", default=0.0, help_text="Sulfate value")
    others = models.FloatField("Others", default=0.0, help_text="Other combined value or 0.0 if none")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Water Analysis"
        verbose_name_plural = "Water Analyses"

    def __str__(self):
        return f"WaterAnalysis #{self.pk or 'unsaved'} — Ca={self.ca} Mg={self.mg} Na={self.na} SO4={self.so4}"

    def as_dict(self):
        """Return a plain dict representation of the numeric values."""
        return {
            "ca": float(self.ca),
            "mg": float(self.mg),
            "na": float(self.na),
            "so4": float(self.so4),
            "others": float(self.others),
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    def from_dict(self, data):
        """Populate fields from a dict of values."""
        self.ca = float(data.get("ca", 0.0))
        self.mg = float(data.get("mg", 0.0))
        self.na = float(data.get("na", 0.0))
        self.so4 = float(data.get("so4", 0.0))
        self.others = float(data.get("others", 0.0))
        return self