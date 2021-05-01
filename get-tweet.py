"""ツイートを取得します"""

#
import twitter

#apikeyの取得




ck=
cs=
at=
ats=

api = twitter.Api(ck,cs,at,ats)
#タイムラインの取得
user = 955610533553557504
statues = api.GetUserTikeline(user)

#出力
print([s.text for s in statuses], '\n')
