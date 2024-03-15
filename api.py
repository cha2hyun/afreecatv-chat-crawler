import requests

def get_player_live(bno, bid):
    url = 'https://live.afreecatv.com/afreeca/player_live_api.php'
    data = {
        'bid': bid,
        'bno': bno,
        'type': 'live',
        'confirm_adult': 'false',
        'player_type': 'html5',
        'mode': 'landing',
        'from_api': '0',
        'pwd': '',
        'stream_type': 'common',
        'quality': 'HD'
    }

    try:
        response = requests.post(f'{url}?bjid={bid}', data=data)
        response.raise_for_status()  # HTTP 요청 에러를 확인하고, 에러가 있을 경우 예외를 발생시킵니다.
        res = response.json()

        CHDOMAIN = res["CHANNEL"]["CHDOMAIN"].lower()
        CHATNO = res["CHANNEL"]["CHATNO"]
        FTK = res["CHANNEL"]["FTK"]
        TITLE = res["CHANNEL"]["TITLE"]
        BJID = res["CHANNEL"]["BJID"]
        CHPT = str(int(res["CHANNEL"]["CHPT"]) + 1)

        return CHDOMAIN, CHATNO, FTK, TITLE, BJID, CHPT

    except requests.RequestException as e:
        print(f"  ERROR: API 요청 중 오류 발생: {e}")
        return None
    except KeyError as e:
        print(f"  ERROR: 응답에서 필요한 데이터를 찾을 수 없습니다: {e}")
        return None