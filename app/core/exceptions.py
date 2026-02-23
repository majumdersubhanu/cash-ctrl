
class CashCtrlException(Exception):
    """Base exception for CashCtrl application."""
    pass

class InSufficientFundsError(CashCtrlException):
    """Raised when an account has insufficient funds for a transaction."""
    pass

class ContactNotFoundError(CashCtrlException):
    """Raised when a P2P contact is not found."""
    pass

class LoanNotFoundError(CashCtrlException):
    """Raised when a loan registry is not found."""
