# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/preferences_widget.ui'
#
# Created: Fri Feb 10 22:50:02 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(757, 771)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 721, 1008))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Miscellaneous", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_3.setContentsMargins(0, -1, 0, 0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.checkbox_immediately_rename = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_immediately_rename.setText(QtGui.QApplication.translate("Form", "Offer to rename new items immediately", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_immediately_rename.setObjectName(_fromUtf8("checkbox_immediately_rename"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_immediately_rename)
        self.checkbox_autoresponse = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_autoresponse.setText(QtGui.QApplication.translate("Form", "Enable auto-response", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_autoresponse.setObjectName(_fromUtf8("checkbox_autoresponse"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkbox_autoresponse)
        self.checkbox_show_random_tips = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_show_random_tips.setText(QtGui.QApplication.translate("Form", "Show random tips on start-up", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_show_random_tips.setObjectName(_fromUtf8("checkbox_show_random_tips"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.checkbox_show_random_tips)
        self.checkbox_toolbar_text = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_toolbar_text.setText(QtGui.QApplication.translate("Form", "Show text in toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_toolbar_text.setObjectName(_fromUtf8("checkbox_toolbar_text"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.checkbox_toolbar_text)
        self.checkbox_new_experiment_dialog = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_new_experiment_dialog.setText(QtGui.QApplication.translate("Form", "Show \'New experiment\' dialog on start-up", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_new_experiment_dialog.setObjectName(_fromUtf8("checkbox_new_experiment_dialog"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.checkbox_new_experiment_dialog)
        self.checkbox_small_toolbar = QtGui.QCheckBox(self.groupBox_2)
        self.checkbox_small_toolbar.setText(QtGui.QApplication.translate("Form", "Small icons in toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_small_toolbar.setObjectName(_fromUtf8("checkbox_small_toolbar"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.checkbox_small_toolbar)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.groupBox_5 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Appearance", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.formLayout_4 = QtGui.QFormLayout(self.groupBox_5)
        self.formLayout_4.setContentsMargins(0, 9, 0, 0)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setText(QtGui.QApplication.translate("Form", "Interface style", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.combobox_style = QtGui.QComboBox(self.groupBox_5)
        self.combobox_style.setObjectName(_fromUtf8("combobox_style"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.combobox_style)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.groupbox_scintilla = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupbox_scintilla.setTitle(QtGui.QApplication.translate("Form", "Embedded text editor", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_scintilla.setObjectName(_fromUtf8("groupbox_scintilla"))
        self.formLayout_5 = QtGui.QFormLayout(self.groupbox_scintilla)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setContentsMargins(0, -1, 0, 0)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.checkbox_scintilla_line_numbers = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_line_numbers.setText(QtGui.QApplication.translate("Form", "Show line numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_line_numbers.setObjectName(_fromUtf8("checkbox_scintilla_line_numbers"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_scintilla_line_numbers)
        self.checkbox_scintilla_folding = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_folding.setText(QtGui.QApplication.translate("Form", "Enable block folding", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_folding.setObjectName(_fromUtf8("checkbox_scintilla_folding"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.checkbox_scintilla_folding)
        self.checkbox_scintilla_right_margin = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_right_margin.setText(QtGui.QApplication.translate("Form", "Show right margin", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_right_margin.setObjectName(_fromUtf8("checkbox_scintilla_right_margin"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkbox_scintilla_right_margin)
        self.checkbox_scintilla_brace_match = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_brace_match.setText(QtGui.QApplication.translate("Form", "Highlight matching braces", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_brace_match.setObjectName(_fromUtf8("checkbox_scintilla_brace_match"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.checkbox_scintilla_brace_match)
        self.checkbox_scintilla_eol_visible = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_eol_visible.setText(QtGui.QApplication.translate("Form", "Show end of lines", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_eol_visible.setObjectName(_fromUtf8("checkbox_scintilla_eol_visible"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.checkbox_scintilla_eol_visible)
        self.checkbox_scintilla_syntax_highlighting = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_syntax_highlighting.setText(QtGui.QApplication.translate("Form", "Enable syntax highlighting", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_syntax_highlighting.setObjectName(_fromUtf8("checkbox_scintilla_syntax_highlighting"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkbox_scintilla_syntax_highlighting)
        self.checkbox_scintilla_whitespace_visible = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_whitespace_visible.setText(QtGui.QApplication.translate("Form", "Show whitespace", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_whitespace_visible.setObjectName(_fromUtf8("checkbox_scintilla_whitespace_visible"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.checkbox_scintilla_whitespace_visible)
        self.checkbox_scintilla_indentation_guides = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_indentation_guides.setText(QtGui.QApplication.translate("Form", "Show indentation guides", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_indentation_guides.setObjectName(_fromUtf8("checkbox_scintilla_indentation_guides"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkbox_scintilla_indentation_guides)
        self.checkbox_scintilla_auto_indent = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_auto_indent.setText(QtGui.QApplication.translate("Form", "Auto indent", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_auto_indent.setObjectName(_fromUtf8("checkbox_scintilla_auto_indent"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.LabelRole, self.checkbox_scintilla_auto_indent)
        self.checkbox_scintilla_custom_font = QtGui.QCheckBox(self.groupbox_scintilla)
        self.checkbox_scintilla_custom_font.setText(QtGui.QApplication.translate("Form", "Use custom font", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_scintilla_custom_font.setObjectName(_fromUtf8("checkbox_scintilla_custom_font"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.checkbox_scintilla_custom_font)
        self.widget_scintilla_font = QtGui.QWidget(self.groupbox_scintilla)
        self.widget_scintilla_font.setEnabled(False)
        self.widget_scintilla_font.setObjectName(_fromUtf8("widget_scintilla_font"))
        self.formLayout_6 = QtGui.QFormLayout(self.widget_scintilla_font)
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setMargin(0)
        self.formLayout_6.setMargin(0)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_4 = QtGui.QLabel(self.widget_scintilla_font)
        self.label_4.setText(QtGui.QApplication.translate("Form", "Font family", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.font_scintilla_font_family = QtGui.QFontComboBox(self.widget_scintilla_font)
        self.font_scintilla_font_family.setObjectName(_fromUtf8("font_scintilla_font_family"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.font_scintilla_font_family)
        self.label_5 = QtGui.QLabel(self.widget_scintilla_font)
        self.label_5.setText(QtGui.QApplication.translate("Form", "Font size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spinbox_scintilla_font_size = QtGui.QSpinBox(self.widget_scintilla_font)
        self.spinbox_scintilla_font_size.setSuffix(QtGui.QApplication.translate("Form", " pt", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_scintilla_font_size.setMinimum(2)
        self.spinbox_scintilla_font_size.setProperty("value", 10)
        self.spinbox_scintilla_font_size.setObjectName(_fromUtf8("spinbox_scintilla_font_size"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinbox_scintilla_font_size)
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.SpanningRole, self.widget_scintilla_font)
        self.verticalLayout_2.addWidget(self.groupbox_scintilla)
        self.line_3 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Form", "Plug-ins", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.formLayout_7 = QtGui.QFormLayout(self.groupBox_6)
        self.formLayout_7.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setContentsMargins(0, 9, 0, 0)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.label_6 = QtGui.QLabel(self.groupBox_6)
        self.label_6.setText(QtGui.QApplication.translate("Form", "Plug-in folders:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.edit_plugin_folders = QtGui.QLineEdit(self.groupBox_6)
        self.edit_plugin_folders.setReadOnly(True)
        self.edit_plugin_folders.setObjectName(_fromUtf8("edit_plugin_folders"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.FieldRole, self.edit_plugin_folders)
        self.widget_plugin_list = QtGui.QWidget(self.groupBox_6)
        self.widget_plugin_list.setObjectName(_fromUtf8("widget_plugin_list"))
        self.layout_plugin_list = QtGui.QVBoxLayout(self.widget_plugin_list)
        self.layout_plugin_list.setMargin(0)
        self.layout_plugin_list.setMargin(0)
        self.layout_plugin_list.setObjectName(_fromUtf8("layout_plugin_list"))
        self.label_plugin_dummy = QtGui.QLabel(self.widget_plugin_list)
        self.label_plugin_dummy.setText(QtGui.QApplication.translate("Form", "Installed plug-ins (deactivation requires restart):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_plugin_dummy.setObjectName(_fromUtf8("label_plugin_dummy"))
        self.layout_plugin_list.addWidget(self.label_plugin_dummy)
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.SpanningRole, self.widget_plugin_list)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.line_4 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Backups", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setContentsMargins(0, 9, 0, 0)
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.checkbox_enable_autosave = QtGui.QCheckBox(self.groupBox)
        self.checkbox_enable_autosave.setText(QtGui.QApplication.translate("Form", "Automatically create backups", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_enable_autosave.setObjectName(_fromUtf8("checkbox_enable_autosave"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_enable_autosave)
        self.label_autosave_interval = QtGui.QLabel(self.groupBox)
        self.label_autosave_interval.setText(QtGui.QApplication.translate("Form", "Auto-save interval:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_autosave_interval.setObjectName(_fromUtf8("label_autosave_interval"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_autosave_interval)
        self.spinbox_autosave_interval = QtGui.QSpinBox(self.groupBox)
        self.spinbox_autosave_interval.setSuffix(QtGui.QApplication.translate("Form", " minute(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_autosave_interval.setPrefix(QtGui.QApplication.translate("Form", "every ", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_autosave_interval.setMinimum(1)
        self.spinbox_autosave_interval.setMaximum(1000)
        self.spinbox_autosave_interval.setSingleStep(10)
        self.spinbox_autosave_interval.setObjectName(_fromUtf8("spinbox_autosave_interval"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinbox_autosave_interval)
        self.button_browse_autosave = QtGui.QPushButton(self.groupBox)
        self.button_browse_autosave.setText(QtGui.QApplication.translate("Form", "Open backup folder", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/browse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_browse_autosave.setIcon(icon)
        self.button_browse_autosave.setObjectName(_fromUtf8("button_browse_autosave"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.button_browse_autosave)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("Form", "Clean backups after:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinbox_autosave_max_age = QtGui.QSpinBox(self.groupBox)
        self.spinbox_autosave_max_age.setSuffix(QtGui.QApplication.translate("Form", " day(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.spinbox_autosave_max_age.setMinimum(1)
        self.spinbox_autosave_max_age.setMaximum(365)
        self.spinbox_autosave_max_age.setObjectName(_fromUtf8("spinbox_autosave_max_age"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinbox_autosave_max_age)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.line_5 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Updates", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, -1, 0, 0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.checkbox_auto_update_check = QtGui.QCheckBox(self.groupBox_3)
        self.checkbox_auto_update_check.setText(QtGui.QApplication.translate("Form", "Check for updates on start-up", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_auto_update_check.setObjectName(_fromUtf8("checkbox_auto_update_check"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkbox_auto_update_check)
        self.button_update_check = QtGui.QPushButton(self.groupBox_3)
        self.button_update_check.setText(QtGui.QApplication.translate("Form", "Check for updates now", None, QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update_check.setIcon(icon1)
        self.button_update_check.setObjectName(_fromUtf8("button_update_check"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.button_update_check)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.line_6 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_2.addWidget(self.line_6)
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Run options", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout.setContentsMargins(0, 9, 0, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">If you experience stability issues, most notably crashes when you run an experiment for the second time in a single session of OpenSesame, you can enable the \'Run experiments in a separate process\' option.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.checkbox_opensesamerun = QtGui.QCheckBox(self.groupBox_4)
        self.checkbox_opensesamerun.setText(QtGui.QApplication.translate("Form", "Run experiments in a separate process", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_opensesamerun.setObjectName(_fromUtf8("checkbox_opensesamerun"))
        self.gridLayout.addWidget(self.checkbox_opensesamerun, 1, 0, 1, 2)
        self.checkbox_auto_opensesamerun_exec = QtGui.QCheckBox(self.groupBox_4)
        self.checkbox_auto_opensesamerun_exec.setText(QtGui.QApplication.translate("Form", "Auto-detect the run command", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_auto_opensesamerun_exec.setObjectName(_fromUtf8("checkbox_auto_opensesamerun_exec"))
        self.gridLayout.addWidget(self.checkbox_auto_opensesamerun_exec, 2, 0, 1, 2)
        self.label_opensesamerun_exec = QtGui.QLabel(self.groupBox_4)
        self.label_opensesamerun_exec.setText(QtGui.QApplication.translate("Form", "Custom run command:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_opensesamerun_exec.setObjectName(_fromUtf8("label_opensesamerun_exec"))
        self.gridLayout.addWidget(self.label_opensesamerun_exec, 3, 0, 1, 1)
        self.edit_opensesamerun_exec = QtGui.QLineEdit(self.groupBox_4)
        self.edit_opensesamerun_exec.setObjectName(_fromUtf8("edit_opensesamerun_exec"))
        self.gridLayout.addWidget(self.edit_opensesamerun_exec, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.checkbox_opensesamerun, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.checkbox_auto_opensesamerun_exec.setEnabled)
        QtCore.QObject.connect(self.checkbox_auto_opensesamerun_exec, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_opensesamerun_exec.setEnabled)
        QtCore.QObject.connect(self.checkbox_auto_opensesamerun_exec, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_opensesamerun_exec.setDisabled)
        QtCore.QObject.connect(self.checkbox_auto_opensesamerun_exec, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.edit_opensesamerun_exec.setDisabled)
        QtCore.QObject.connect(self.checkbox_enable_autosave, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinbox_autosave_interval.setEnabled)
        QtCore.QObject.connect(self.checkbox_enable_autosave, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_autosave_interval.setEnabled)
        QtCore.QObject.connect(self.checkbox_scintilla_custom_font, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.widget_scintilla_font.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

