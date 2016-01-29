import consts


class BaseException(Exception):
    message = 'dark chess base exception'


class BaseArgException(BaseException):
    def __init__(self, *args, **kwargs):
        self.message = self.message.format(*args, **kwargs)
        super(BaseArgException, self).__init__(*args, **kwargs)


class OutOfBoardError(BaseException):
    message = 'coordinates are out of board'


class CellIsBusyError(BaseException):
    message = 'you cannot cut your figure'


class WrongMoveError(BaseException):
    message = 'wrong move'


class WrongFigureError(BaseException):
    message = 'you can move only your figures'


class WrongTurnError(BaseException):
    message = 'it is not your turn'


class NotFoundError(BaseException):
    message = 'figure not found'


class EndGame(BaseException):
    message = 'game is over'
    reason = consts.UNKNOWN


class WhiteWon(EndGame):
    message = 'white player won'
    reason = consts.END_CHECKMATE


class BlackWon(EndGame):
    message = 'black player won'
    reason = consts.END_CHECKMATE


class Draw(EndGame):
    message = 'draw'
    reason = consts.END_DRAW


class GameNotFoundError(BaseException):
    message = 'game not found'


class TooOftenRequestError(BaseArgException):
    message = 'too often requests, try again after {} seconds'


class VerifiedError(BaseException):
    message = 'your email is already verified'


class VerificationRequestError(BaseArgException):
    message = 'you must wait {} seconds to get new verification code'


class ValidationError(BaseArgException):
    message = '{} is not valid'


class ValidationRequiredError(ValidationError):
    message = '{} is required'
