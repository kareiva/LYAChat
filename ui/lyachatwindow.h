#ifndef LYACHATWINDOW_H
#define LYACHATWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class LYAChatWindow; }
QT_END_NAMESPACE

class LYAChatWindow : public QMainWindow
{
    Q_OBJECT

public:
    LYAChatWindow(QWidget *parent = nullptr);
    ~LYAChatWindow();

private:
    Ui::LYAChatWindow *ui;
};
#endif // LYACHATWINDOW_H
