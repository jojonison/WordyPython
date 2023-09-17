# Python stubs generated by omniidl from Wordy.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "common"
#
__name__ = "common"
_0_common = omniORB.openModule("common", r"Wordy.idl")
_0_common__POA = omniORB.openModule("common__POA", r"Wordy.idl")


# struct TopPlayers
_0_common.TopPlayers = omniORB.newEmptyClass()
class TopPlayers (omniORB.StructBase):
    _NP_RepositoryId = "IDL:common/TopPlayers:1.0"

    def __init__(self, username, rank, numberOfWins):
        self.username = username
        self.rank = rank
        self.numberOfWins = numberOfWins

_0_common.TopPlayers = TopPlayers
_0_common._d_TopPlayers  = (omniORB.tcInternal.tv_struct, TopPlayers, TopPlayers._NP_RepositoryId, "TopPlayers", "username", (omniORB.tcInternal.tv_string,0), "rank", omniORB.tcInternal.tv_long, "numberOfWins", omniORB.tcInternal.tv_long)
_0_common._tc_TopPlayers = omniORB.tcInternal.createTypeCode(_0_common._d_TopPlayers)
omniORB.registerType(TopPlayers._NP_RepositoryId, _0_common._d_TopPlayers, _0_common._tc_TopPlayers)
del TopPlayers

# struct TopWords
_0_common.TopWords = omniORB.newEmptyClass()
class TopWords (omniORB.StructBase):
    _NP_RepositoryId = "IDL:common/TopWords:1.0"

    def __init__(self, theWord, username, rank):
        self.theWord = theWord
        self.username = username
        self.rank = rank

_0_common.TopWords = TopWords
_0_common._d_TopWords  = (omniORB.tcInternal.tv_struct, TopWords, TopWords._NP_RepositoryId, "TopWords", "theWord", (omniORB.tcInternal.tv_string,0), "username", (omniORB.tcInternal.tv_string,0), "rank", omniORB.tcInternal.tv_long)
_0_common._tc_TopWords = omniORB.tcInternal.createTypeCode(_0_common._d_TopWords)
omniORB.registerType(TopWords._NP_RepositoryId, _0_common._d_TopWords, _0_common._tc_TopWords)
del TopWords

# typedef ... TopFivePlayersSequence
class TopFivePlayersSequence:
    _NP_RepositoryId = "IDL:common/TopFivePlayersSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_common.TopFivePlayersSequence = TopFivePlayersSequence
_0_common._d_TopFivePlayersSequence  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:common/TopPlayers:1.0"], 0)
_0_common._ad_TopFivePlayersSequence = (omniORB.tcInternal.tv_alias, TopFivePlayersSequence._NP_RepositoryId, "TopFivePlayersSequence", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:common/TopPlayers:1.0"], 0))
_0_common._tc_TopFivePlayersSequence = omniORB.tcInternal.createTypeCode(_0_common._ad_TopFivePlayersSequence)
omniORB.registerType(TopFivePlayersSequence._NP_RepositoryId, _0_common._ad_TopFivePlayersSequence, _0_common._tc_TopFivePlayersSequence)
del TopFivePlayersSequence

# typedef ... TopFiveWordsSequence
class TopFiveWordsSequence:
    _NP_RepositoryId = "IDL:common/TopFiveWordsSequence:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_common.TopFiveWordsSequence = TopFiveWordsSequence
_0_common._d_TopFiveWordsSequence  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:common/TopWords:1.0"], 0)
_0_common._ad_TopFiveWordsSequence = (omniORB.tcInternal.tv_alias, TopFiveWordsSequence._NP_RepositoryId, "TopFiveWordsSequence", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:common/TopWords:1.0"], 0))
_0_common._tc_TopFiveWordsSequence = omniORB.tcInternal.createTypeCode(_0_common._ad_TopFiveWordsSequence)
omniORB.registerType(TopFiveWordsSequence._NP_RepositoryId, _0_common._ad_TopFiveWordsSequence, _0_common._tc_TopFiveWordsSequence)
del TopFiveWordsSequence

# exception WordIsInvalid
_0_common.WordIsInvalid = omniORB.newEmptyClass()
class WordIsInvalid (CORBA.UserException):
    _NP_RepositoryId = "IDL:common/WordIsInvalid:1.0"

    def __init__(self, exceptionMessage):
        CORBA.UserException.__init__(self, exceptionMessage)
        self.exceptionMessage = exceptionMessage

_0_common.WordIsInvalid = WordIsInvalid
_0_common._d_WordIsInvalid  = (omniORB.tcInternal.tv_except, WordIsInvalid, WordIsInvalid._NP_RepositoryId, "WordIsInvalid", "exceptionMessage", (omniORB.tcInternal.tv_string,0))
_0_common._tc_WordIsInvalid = omniORB.tcInternal.createTypeCode(_0_common._d_WordIsInvalid)
omniORB.registerType(WordIsInvalid._NP_RepositoryId, _0_common._d_WordIsInvalid, _0_common._tc_WordIsInvalid)
del WordIsInvalid

# exception RanOutOfTime
_0_common.RanOutOfTime = omniORB.newEmptyClass()
class RanOutOfTime (CORBA.UserException):
    _NP_RepositoryId = "IDL:common/RanOutOfTime:1.0"

    def __init__(self, exceptionMessage):
        CORBA.UserException.__init__(self, exceptionMessage)
        self.exceptionMessage = exceptionMessage

_0_common.RanOutOfTime = RanOutOfTime
_0_common._d_RanOutOfTime  = (omniORB.tcInternal.tv_except, RanOutOfTime, RanOutOfTime._NP_RepositoryId, "RanOutOfTime", "exceptionMessage", (omniORB.tcInternal.tv_string,0))
_0_common._tc_RanOutOfTime = omniORB.tcInternal.createTypeCode(_0_common._d_RanOutOfTime)
omniORB.registerType(RanOutOfTime._NP_RepositoryId, _0_common._d_RanOutOfTime, _0_common._tc_RanOutOfTime)
del RanOutOfTime

# exception NoOtherPlayersJoined
_0_common.NoOtherPlayersJoined = omniORB.newEmptyClass()
class NoOtherPlayersJoined (CORBA.UserException):
    _NP_RepositoryId = "IDL:common/NoOtherPlayersJoined:1.0"

    def __init__(self, exceptionMessage):
        CORBA.UserException.__init__(self, exceptionMessage)
        self.exceptionMessage = exceptionMessage

_0_common.NoOtherPlayersJoined = NoOtherPlayersJoined
_0_common._d_NoOtherPlayersJoined  = (omniORB.tcInternal.tv_except, NoOtherPlayersJoined, NoOtherPlayersJoined._NP_RepositoryId, "NoOtherPlayersJoined", "exceptionMessage", (omniORB.tcInternal.tv_string,0))
_0_common._tc_NoOtherPlayersJoined = omniORB.tcInternal.createTypeCode(_0_common._d_NoOtherPlayersJoined)
omniORB.registerType(NoOtherPlayersJoined._NP_RepositoryId, _0_common._d_NoOtherPlayersJoined, _0_common._tc_NoOtherPlayersJoined)
del NoOtherPlayersJoined

# exception LogInException
_0_common.LogInException = omniORB.newEmptyClass()
class LogInException (CORBA.UserException):
    _NP_RepositoryId = "IDL:common/LogInException:1.0"

    def __init__(self, exceptionMessage):
        CORBA.UserException.__init__(self, exceptionMessage)
        self.exceptionMessage = exceptionMessage

_0_common.LogInException = LogInException
_0_common._d_LogInException  = (omniORB.tcInternal.tv_except, LogInException, LogInException._NP_RepositoryId, "LogInException", "exceptionMessage", (omniORB.tcInternal.tv_string,0))
_0_common._tc_LogInException = omniORB.tcInternal.createTypeCode(_0_common._d_LogInException)
omniORB.registerType(LogInException._NP_RepositoryId, _0_common._d_LogInException, _0_common._tc_LogInException)
del LogInException

# interface GameFunctions
_0_common._d_GameFunctions = (omniORB.tcInternal.tv_objref, "IDL:common/GameFunctions:1.0", "GameFunctions")
omniORB.typeMapping["IDL:common/GameFunctions:1.0"] = _0_common._d_GameFunctions
_0_common.GameFunctions = omniORB.newEmptyClass()
class GameFunctions :
    _NP_RepositoryId = _0_common._d_GameFunctions[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_common.GameFunctions = GameFunctions
_0_common._tc_GameFunctions = omniORB.tcInternal.createTypeCode(_0_common._d_GameFunctions)
omniORB.registerType(GameFunctions._NP_RepositoryId, _0_common._d_GameFunctions, _0_common._tc_GameFunctions)

# GameFunctions operations and attributes
GameFunctions._d_logIn = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), {_0_common.LogInException._NP_RepositoryId: _0_common._d_LogInException})
GameFunctions._d_logOut = (((omniORB.tcInternal.tv_string,0), ), (), None)
GameFunctions._d_playGame = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_long, ), {_0_common.NoOtherPlayersJoined._NP_RepositoryId: _0_common._d_NoOtherPlayersJoined})
GameFunctions._d_bringItOn = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)
GameFunctions._d_getTimer = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_long, ), None)
GameFunctions._d_whoWonTheRound = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)
GameFunctions._d_whoWonTheGame = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)
GameFunctions._d_sendAWord = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), {_0_common.WordIsInvalid._NP_RepositoryId: _0_common._d_WordIsInvalid, _0_common.RanOutOfTime._NP_RepositoryId: _0_common._d_RanOutOfTime})
GameFunctions._d_getTheSeventeenLetters = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)
GameFunctions._d_getTopFivePlayers = ((), (omniORB.typeMapping["IDL:common/TopFivePlayersSequence:1.0"], ), None)
GameFunctions._d_getTopFiveLongestWords = ((), (omniORB.typeMapping["IDL:common/TopFiveWordsSequence:1.0"], ), None)

# GameFunctions object reference
class _objref_GameFunctions (CORBA.Object):
    _NP_RepositoryId = GameFunctions._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def logIn(self, *args):
        return self._obj.invoke("logIn", _0_common.GameFunctions._d_logIn, args)

    def logOut(self, *args):
        return self._obj.invoke("logOut", _0_common.GameFunctions._d_logOut, args)

    def playGame(self, *args):
        return self._obj.invoke("playGame", _0_common.GameFunctions._d_playGame, args)

    def bringItOn(self, *args):
        return self._obj.invoke("bringItOn", _0_common.GameFunctions._d_bringItOn, args)

    def getTimer(self, *args):
        return self._obj.invoke("getTimer", _0_common.GameFunctions._d_getTimer, args)

    def whoWonTheRound(self, *args):
        return self._obj.invoke("whoWonTheRound", _0_common.GameFunctions._d_whoWonTheRound, args)

    def whoWonTheGame(self, *args):
        return self._obj.invoke("whoWonTheGame", _0_common.GameFunctions._d_whoWonTheGame, args)

    def sendAWord(self, *args):
        return self._obj.invoke("sendAWord", _0_common.GameFunctions._d_sendAWord, args)

    def getTheSeventeenLetters(self, *args):
        return self._obj.invoke("getTheSeventeenLetters", _0_common.GameFunctions._d_getTheSeventeenLetters, args)

    def getTopFivePlayers(self, *args):
        return self._obj.invoke("getTopFivePlayers", _0_common.GameFunctions._d_getTopFivePlayers, args)

    def getTopFiveLongestWords(self, *args):
        return self._obj.invoke("getTopFiveLongestWords", _0_common.GameFunctions._d_getTopFiveLongestWords, args)

omniORB.registerObjref(GameFunctions._NP_RepositoryId, _objref_GameFunctions)
_0_common._objref_GameFunctions = _objref_GameFunctions
del GameFunctions, _objref_GameFunctions

# GameFunctions skeleton
__name__ = "common__POA"
class GameFunctions (PortableServer.Servant):
    _NP_RepositoryId = _0_common.GameFunctions._NP_RepositoryId


    _omni_op_d = {"logIn": _0_common.GameFunctions._d_logIn, "logOut": _0_common.GameFunctions._d_logOut, "playGame": _0_common.GameFunctions._d_playGame, "bringItOn": _0_common.GameFunctions._d_bringItOn, "getTimer": _0_common.GameFunctions._d_getTimer, "whoWonTheRound": _0_common.GameFunctions._d_whoWonTheRound, "whoWonTheGame": _0_common.GameFunctions._d_whoWonTheGame, "sendAWord": _0_common.GameFunctions._d_sendAWord, "getTheSeventeenLetters": _0_common.GameFunctions._d_getTheSeventeenLetters, "getTopFivePlayers": _0_common.GameFunctions._d_getTopFivePlayers, "getTopFiveLongestWords": _0_common.GameFunctions._d_getTopFiveLongestWords}

GameFunctions._omni_skeleton = GameFunctions
_0_common__POA.GameFunctions = GameFunctions
omniORB.registerSkeleton(GameFunctions._NP_RepositoryId, GameFunctions)
del GameFunctions
__name__ = "common"

#
# End of module "common"
#
__name__ = "Wordy_idl"

_exported_modules = ( "common", )

# The end.
