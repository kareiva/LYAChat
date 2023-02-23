#include "lyachatwindow.h"
#include "ui_lyachatwindow.h"

LYAChatWindow::LYAChatWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::LYAChatWindow)
{
    ui->setupUi(this);
}

LYAChatWindow::~LYAChatWindow()
{
    delete ui;
}

