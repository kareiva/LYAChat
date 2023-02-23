#include "lyachatwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    LYAChatWindow w;
    w.show();
    return a.exec();
}
