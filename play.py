import requests
#

key = 'heKMs79VhvSRvCO3oaBWTh18ixarr7ck-UBo0N1YiiQ'



# r = requests.get('https://dev-770962.okta.com/oauth2/', data=data)
r = requests.get(f'https://dev-770962.okta.com/oauth2/logout?id_token_hint=${key}')

print(r)


# headers = {
#     'Content-type': 'application/x-www-form-urlencoded',
# }
#
# data = {
#     'client_id': '0oaof5bb45s7JQgyV4x6',
#     'client_secret': '4htsnjxX_g8Rxe5zbyscaf1vruOKIdzBrRCGKf3B',
#     'grant_type': 'authorization_code',
#     'redirect_uri': 'http://127.0.0.1:8001/oidc/callback',
#     'code': '{code}'
# }
#
# response = requests.post('https://dev-770962.okta.com/oauth2/default/v1/token', headers=headers, data=data)
#
# print(response.text)
#
