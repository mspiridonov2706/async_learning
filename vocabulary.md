## Процесс
*Процесс* - работающее приложение, которому выделена
область памяти, недоступная другим приложениям

>Пример создания Python-процесса – запуск простого приложения «hello world» или
ввод слова python в командной строке для запуска цикла REPL (цикл чтения–вычисления–печати).

>На одной машине может работать несколько процессов. Если машина оснащена процессором с несколькими ядрами, то несколь ко процессов могут работать одновременно. Если процессор имеет только одно ядро, то все равно можно выполнять несколько приложений конкурентно, но уже с применением квантования времени.

## Поток
*Поток* - облегченные процессы. Кроме того, это наименьшая единица выполнения, которая может управляться операционной системой.

>У потоков нет своей памяти, они пользуются памятью создавшего их процесса. Потоки ассоциированы с процессом, создавшим их. С каждым процессом всегда ассоциирован по меньшей мере один поток, обычно называемый главным.

>Процесс может создавать дополнительные потоки, которые обычно называются рабочими или фоновыми. Эти потоки могут конкурентно выполнять другую работу наряду с главным потоком. Потоки, как и процессы, могут работать параллельно на многоядерном процессе, и операционная система может переключаться между ними с помощью квантования времени. Обычное Python-приложение создает процесс и главный поток, который отвечает за его выполнение.

## Сопрограмма
*Сопрограмма* – это метод, который можно приостановить, если имеется потенциально длительная задача, а затем
возобновить, когда она завершится

> Сопрограмму можно рассматривать как обычную функцию Python, наделенную сверхспособностью: приостанавливаться,
встретив операцию, для выполнения которой нужно заметное время. 
По завершении такой длительной операции сопрограмму можно «пробудить», после чего она продолжит выполнение. 
Пока приостановленная сопрограмма ждет завершения операции, мы можем выполнять другой код.

## GIL - Global interpretator lock
*GIL* – не дает Python-процессу исполнять более одной команды байт-кода
в каждый момент времени. Это означает, что, даже если имеется несколько потоков на многоядерной машине, интерпретатор сможет в каждый момент исполнять только один поток, содержащий написанный на Python код. У каждого Python-процесса своя собственная GIL.

> Глобальная блокировка интерпретатора освобождается на время
выполнения операций ввода-вывода

## Сокет
*Сокет* – это низкоуровневая абстракция отправки и получения данных по сети.

> Именно с ее помощью производится обмен данными между клиентами и серверами. Сокеты поддерживают две основные операции: отправку и получение байтов. Мы записываем байты в сокет, затем они передаются по адресу назначения, чаще всего на какой-то сервер. Отправив байты, мы ждем, пока сервер пришлет ответ в наш сокет. Когда байты окажутся в сокете, мы сможем прочитать результат.

## Цикл событий
*Цикл событий* – мы создаем очередь, в которой хранится список задач, а затем входим в бесконечный цикл, где обрабатываем задачи (обёртка для сопрограммы) по мере их поступления. Сопрограмма может приостановить выполнение, встретив операцию ввода-вывода, и дать циклу событий возможность выполнить другие задачи, которые не ждут завершения ввода-вывода.

> Создавая цикл событий, мы создаем пустую очередь задач. Затем добавляем в эту очередь задачи для выполнения. На каждой итерации цикла проверяется, есть ли в очереди готовая задача, и если да, то она выполняется, пока не встретит операцию ввода-вывода. В этот момент задача приостанавливается, и мы просим операционную систему наблюдать за ее сокетами. А сами тем временем переходим к следующей готовой задаче. На каждой итерации проверяется, завершилась ли какая-нибудь операция ввода-вывода; если да, то ожидавшие ее завершения задачи пробуждаются и им предоставляется возможность продолжить работу.