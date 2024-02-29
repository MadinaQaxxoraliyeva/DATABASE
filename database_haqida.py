"""
1.CREATE DATABASE databasenomi ==>> ma_lumotlar omborini yaratadi
2.DROP DATABASE databasenomi ==>> ma_lumotlar omborini o'chiradi
\l ==>> database list yani ma_lumotlar omborini ro'yxatini ko'rsatadi
\d ==>> database table yani ombordagi jadvallar ro'yxatini ko'rishimiz mn
\! cls ==>> clean yani oynani tozalaydi
\c ==>> connect database yani kerakli databasega o'tib olish
\du ==>> in database superusers yani superadminlar ro'yxatini ko'rsatadi
\!d tablename ==>> bu jadval nomlarini korsatadi
"""

# SQL  tili ma'lumotlarni o'z tarkibida jadvallarda saqlab boradi:
"""
DB ==>>TABLE==>> columns and rows :
"""
# TEXT 3 xil turga bo'linadi:
"""
Varchar ==>> limit bolganida ishlatamiz:   varchar(10)
Text ==>> limiti bo'lmaganda ishlatamiz,
Char ==>> varchar bn bir xil farqi doim berilgan uzunlikkacha belgi oladi agar 
yetmasa 'space' qo'shib qo'yadi
"""
# INTEGER 3 turga bo'linadi:
"""
Int ==>> (4 baitlik ) sonlarni ifodalaydi va xuddi shuningdek musbat va manfiy sonlarni ham ifodalaydi yani
odatda -2,147,483,648 dan 2,147,483,647 gacha sonlarni qabul qiladi
SMALLINT ==>> u kichik sonlar un ishlatladi. 16 bitlik sonlarni ifodalaydi va odatda -32,768 dan 32,767 gacha 
sonlarni qabul qiladi
BIGINT ==>> u  katta sonlarni ifodalsh un ishlatiladi. 64 bitlik sonlarni ifodalaydi va odatda 
-9,223,372,036,854,775,808 dan 9,223,372,036,854,775,807 gacha bolgan sonlarni qabul qiladi
"""

"""
SERIAL ==>> int bn bir xil faqat buni postgresql o'zi joylashtirib beradi.

MYSQL  buning o'rniga eqvivalenti AUTOINCREMENT;
Smallserial, serial, bigserial kabi;

Numeric ==>> numeric(5,2) bunda jami sonlar 5 tadan keyin esa 2 deb tushunsak bo'ladi.
(256.25,215,256 ==>> 215.26)
Numeric(5) ==>> bunda faqat 5 xonali sonlar deyiladi(12345,11111)(defalut(0));
Numeric ==>> istalgancha raqam
Boolean ==>> true yoki false ;
"""
# VAQTLAR:
"""
DATE ==>> sanalar ==>> 2024-02-29
TIME ==>> vaqt uchun ==>> 16:33:25;
TIMESTAMP==>> ikkalasi xam ==>> 2024-02-29 16:33:25
"""