def user_info(name, surname, birthday, city, e_mail, phone):
    if phone.isdigit():
        if '@' in e_mail and '.' in e_mail:
            print(name, surname, birthday, city,' e-mail: ', e_mail, 'phone: ', phone)
        else:
            print('неверный формат данных в e-mail')
    else:
        print('номер телефона должен состоять из букв')


user_info(name='Leonardo', surname='Dicaprio', birthday=1974, city='Hollywood', e_mail='Leonardo@gmail.com', phone= '0017777777')