import csv
import io
import json
import uuid
from typing import Sequence
from fastapi.responses import StreamingResponse
from app.models.transaction import Transaction

class ReportService:
    def export_transactions_csv(self, transactions: Sequence[Transaction]) -> io.StringIO:
        """
        Generates a CSV report of transactions.
        """
        output = io.StringIO()
        writer = csv.writer(output)
