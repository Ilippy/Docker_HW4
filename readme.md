# Семинар 4
## Инструкция
```
sudo su					    # переходим в root 
mkdir mkdir hw4 && cd hw4	            # создаем папку hw4 и переходим туда
nano main.py				    # cоздаем питоновский файл main.py и заполняем его
```
![Screenshot_87.png](img%2FScreenshot_87.png)
```
nano Dockerfile				        # создаем Dockerfile
```
![Screenshot_88.png](img%2FScreenshot_88.png)
```
docker build -t scrap-movie .			# создаем образ scrap-movie по Dockerfile
docker run -ti --name scrap-movie scrap-movie
# создаем контейнер по образу scrap-movie в интерактивном режиме
```
![Screenshot_89.png](img%2FScreenshot_89.png)