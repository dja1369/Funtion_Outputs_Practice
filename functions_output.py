#함수와 출력에 대한 연습.

#title은 모든 문자열을 되돌린후 첫번째 글자만 대문자로 변경한다.
def format_name(f_name, l_name):
      formated_f_name = f_name.title()
      formated_ㅣ_name = l_name.title()
      return f"{formated_f_name},{formated_ㅣ_name}"


you = format_name("angela","yomimoto")
print(you)