from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


"""Create button for create, view, edit shedule"""
shedule_mrkup = InlineKeyboardMarkup(row_width=1)
shedule_create_frofile_btn = InlineKeyboardButton(
    text='Создать профиль',
    callback_data='createfrofile'
)
shedule_create_btn = InlineKeyboardButton(
    text='Создать расписание',
    callback_data='createshedule'
)
shedule_view_btn = InlineKeyboardButton(
    text='Просмотреть запись',
    callback_data='viewshedule'
)
shedule_edit_btn = InlineKeyboardButton(
    text='Изменить расписание',
    callback_data='editshedule'
)
shedule_change_profile_btn = InlineKeyboardButton(
    text='Изменить профиль',
    callback_data='changeprofile'
)

shedule_mrkup.add(shedule_create_frofile_btn,
                  shedule_create_btn,
                  shedule_view_btn,
                  shedule_edit_btn,
                  shedule_change_profile_btn
                  )
