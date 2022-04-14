# Twittor
使用Flask模仿Twitter頁面的練習，並將其部屬到Heroku平台上。
(練習時使用sqllite，部屬使用Mysql)

部屬網址:https://flask-twittor.herokuapp.com/

功能一覽:

![Log IN](https://user-images.githubusercontent.com/38405117/163371496-fd8ad61a-00db-400c-98c2-c4918c2be76b.png)

網站設計用戶必須登入才能瀏覽，登入後可以發推文、編輯個人檔案，探索及追蹤其他用戶。

![index](https://user-images.githubusercontent.com/38405117/163371785-85978fa6-9846-4940-a9ac-cd33d3d8dd5a.JPG)

當用戶註冊時，註冊密碼會以hash值儲存以保護密碼。

![image](https://user-images.githubusercontent.com/38405117/163374858-c4f23611-e582-419d-bc0e-4a1a226a4c32.png)

在mysql中儲存3張Table，user儲存用戶的基本資料，tweet儲存用戶發文，follower則是利用外部鍵儲存前兩張Table的關係。以達成在首頁顯示自己和已追蹤用戶的發文。

![image](https://user-images.githubusercontent.com/38405117/163376644-95b54c7d-b0f2-4279-b98f-54a25ac94d81.png)

當用戶忘記密碼時，可以輸入email地址獲得重設密碼的信(當email未註冊時會提示用戶未註冊)

![image](https://user-images.githubusercontent.com/38405117/163378249-299cc01f-f0ed-459e-8930-c72629d44491.png)


部屬平台選擇Heroku，利用git建構專案，並運用Heroku上的ClearDB(Mysql)作為線上的資料庫，WSGI選擇gunicorn。
