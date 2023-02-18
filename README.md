# Moodle News Bot


## EN

During the Covid pandemic and distance learning, Moodle was an indispensable tool for assignments, announcements and content sharing. Students were required to follow the pages of all courses. This was a difficult task as we had more than 10 courses to check. That's why I developed a Discord bot that periodically visits the pages of all courses and, when a change is detected, sends a message notifying the change to the page. I worked on this project from the end of 2020 to the beginning of 2021. With the end of distance education, the project was terminated.

The bot opens a headless web browser using Selenium and webscrapes the contents using BeautifulSoup4 and saves it in a .txt file. Then it determines if there is any difference. If there is, it sends the changed part as a message to the specified Discord channel and saves the last version of contents for further comparisons. This cycle repeats periodically. The difference is determined  by comparing the last scrape

## TR

Covid salgını ve uzaktan eğitim sırasında Moodle, ödevler, duyurular ve içerik paylaşımı için vazgeçilmez bir araçtı. Öğrencilerin tüm derslerin sayfalarını takip etmesi gerekiyordu. Kontrol etmemiz gereken 10'dan fazla ders olduğu için bu zor bir görevdi. Bu nedenle, tüm derslerin sayfalarını periyodik olarak ziyaret eden ve bir değişiklik tespit edildiğinde sayfadaki değişikliği bildiren bir mesaj gönderen bir Discord botu geliştirdim. 2020'nin sonundan 2021'in başına kadar bu proje üzerinde çalıştım. Uzaktan eğitimin sona ermesiyle birlikte proje sonlandırıldı.

Bot, Selenium'u kullanarak başsız bir web tarayıcısı açar ve BeautifulSoup4'ü kullanarak içeriği veri kazıma ile elde eder. Sonra herhangi bir fark olup olmadığını belirler. Varsa değiştirilen kısmı belirtilen Discord kanalına mesaj olarak gönderir ve içeriğin son versiyonunu sonraki karşılaştırmalar için kaydeder. Bu döngü periyodik olarak tekrar eder.

![](https://user-images.githubusercontent.com/118119029/219814077-1e840b04-230b-458e-89ac-7c4ab1c6ef51.png)
