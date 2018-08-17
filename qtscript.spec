#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtscript
Version  : 5.11.1
Release  : 10
URL      : http://download.qt.io/official_releases/qt/5.11/5.11.1/submodules/qtscript-everywhere-src-5.11.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.11/5.11.1/submodules/qtscript-everywhere-src-5.11.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-3.0
Requires: qtscript-lib
Requires: qtscript-license
Requires: qtscript-extras
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5UiTools)
BuildRequires : pkgconfig(Qt5Widgets)

%description
Qt is provided with a powerful embedded scripting environment through the Qt Script
classes.

%package dev
Summary: dev components for the qtscript package.
Group: Development
Requires: qtscript-lib
Provides: qtscript-devel

%description dev
dev components for the qtscript package.


%package extras
Summary: extras components for the qtscript package.
Group: Default

%description extras
extras components for the qtscript package.


%package lib
Summary: lib components for the qtscript package.
Group: Libraries
Requires: qtscript-license

%description lib
lib components for the qtscript package.


%package license
Summary: license components for the qtscript package.
Group: Default

%description license
license components for the qtscript package.


%prep
%setup -q -n qtscript-everywhere-src-5.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1534487481
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/qtscript
cp LICENSE.FDL %{buildroot}/usr/share/doc/qtscript/LICENSE.FDL
cp LICENSE.GPL2 %{buildroot}/usr/share/doc/qtscript/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/doc/qtscript/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/doc/qtscript/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/doc/qtscript/LICENSE.LGPL3
cp src/3rdparty/javascriptcore/JavaScriptCore/COPYING.LIB %{buildroot}/usr/share/doc/qtscript/src_3rdparty_javascriptcore_JavaScriptCore_COPYING.LIB
cp src/3rdparty/javascriptcore/JavaScriptCore/pcre/COPYING %{buildroot}/usr/share/doc/qtscript/src_3rdparty_javascriptcore_JavaScriptCore_pcre_COPYING
cp tests/benchmarks/script/sunspider/tests/LICENSE.txt %{buildroot}/usr/share/doc/qtscript/tests_benchmarks_script_sunspider_tests_LICENSE.txt
cp tests/benchmarks/script/v8/tests/LICENSE.txt %{buildroot}/usr/share/doc/qtscript/tests_benchmarks_script_v8_tests_LICENSE.txt
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptable_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptactivationobject_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptast_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptastfwd_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptastvisitor_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptclassobject_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptcontext_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptdeclarativeclass_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptdeclarativeobject_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptengine_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptengineagent_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptfunction_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptglobalobject_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptgrammar_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptlexer_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptobject_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptparser_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptprogram_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptqobject_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptstaticscopeobject_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptstring_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptsyntaxchecker_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptvalue_p.h
/usr/include/qt5/QtScript/5.11.1/QtScript/private/qscriptvariant_p.h
/usr/include/qt5/QtScript/QScriptClass
/usr/include/qt5/QtScript/QScriptClassPropertyIterator
/usr/include/qt5/QtScript/QScriptContext
/usr/include/qt5/QtScript/QScriptContextInfo
/usr/include/qt5/QtScript/QScriptContextInfoList
/usr/include/qt5/QtScript/QScriptEngine
/usr/include/qt5/QtScript/QScriptEngineAgent
/usr/include/qt5/QtScript/QScriptExtensionInterface
/usr/include/qt5/QtScript/QScriptExtensionPlugin
/usr/include/qt5/QtScript/QScriptProgram
/usr/include/qt5/QtScript/QScriptString
/usr/include/qt5/QtScript/QScriptSyntaxCheckResult
/usr/include/qt5/QtScript/QScriptValue
/usr/include/qt5/QtScript/QScriptValueIterator
/usr/include/qt5/QtScript/QScriptValueList
/usr/include/qt5/QtScript/QScriptable
/usr/include/qt5/QtScript/QtScript
/usr/include/qt5/QtScript/QtScriptDepends
/usr/include/qt5/QtScript/QtScriptVersion
/usr/include/qt5/QtScript/qscriptable.h
/usr/include/qt5/QtScript/qscriptclass.h
/usr/include/qt5/QtScript/qscriptclasspropertyiterator.h
/usr/include/qt5/QtScript/qscriptcontext.h
/usr/include/qt5/QtScript/qscriptcontextinfo.h
/usr/include/qt5/QtScript/qscriptengine.h
/usr/include/qt5/QtScript/qscriptengineagent.h
/usr/include/qt5/QtScript/qscriptextensioninterface.h
/usr/include/qt5/QtScript/qscriptextensionplugin.h
/usr/include/qt5/QtScript/qscriptprogram.h
/usr/include/qt5/QtScript/qscriptstring.h
/usr/include/qt5/QtScript/qscriptvalue.h
/usr/include/qt5/QtScript/qscriptvalueiterator.h
/usr/include/qt5/QtScript/qtscriptglobal.h
/usr/include/qt5/QtScript/qtscriptversion.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptbreakpointdata_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptbreakpointsmodel_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptbreakpointswidget_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptbreakpointswidgetinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptbreakpointswidgetinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptcompletionproviderinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptcompletiontask_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptcompletiontaskinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptcompletiontaskinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebugger_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggeragent_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggeragent_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerbackend_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerbackend_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercodefinderwidget_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercodefinderwidgetinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercodefinderwidgetinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercodeview_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercodeviewinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercodeviewinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercodewidget_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercodewidgetinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercodewidgetinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercommand_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercommandexecutor_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercommandschedulerfrontend_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercommandschedulerinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercommandschedulerjob_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggercommandschedulerjob_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsole_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolecommand_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolecommand_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolecommandgroupdata_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolecommandjob_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolecommandjob_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolecommandmanager_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsoleglobalobject_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolehistorianinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolewidget_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolewidgetinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerconsolewidgetinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerevent_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggereventhandlerinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerfrontend_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerfrontend_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerjob_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerjob_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerjobschedulerinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerlocalsmodel_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerlocalswidget_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerlocalswidgetinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerlocalswidgetinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerobjectsnapshotdelta_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerresponse_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerresponsehandlerinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerscriptedconsolecommand_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerscriptsmodel_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerscriptswidget_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerscriptswidgetinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerscriptswidgetinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerstackmodel_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerstackwidget_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerstackwidgetinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerstackwidgetinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerstandardwidgetfactory_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggervalue_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggervalueproperty_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebuggerwidgetfactoryinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebugoutputwidget_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebugoutputwidgetinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptdebugoutputwidgetinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptedit_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptenginedebuggerfrontend_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscripterrorlogwidget_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscripterrorlogwidgetinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscripterrorlogwidgetinterface_p_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptmessagehandlerinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptobjectsnapshot_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptscriptdata_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptstdmessagehandler_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptsyntaxhighlighter_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscripttooltipproviderinterface_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptvalueproperty_p.h
/usr/include/qt5/QtScriptTools/5.11.1/QtScriptTools/private/qscriptxmlparser_p.h
/usr/include/qt5/QtScriptTools/QScriptEngineDebugger
/usr/include/qt5/QtScriptTools/QtScriptTools
/usr/include/qt5/QtScriptTools/QtScriptToolsDepends
/usr/include/qt5/QtScriptTools/QtScriptToolsVersion
/usr/include/qt5/QtScriptTools/qscriptenginedebugger.h
/usr/include/qt5/QtScriptTools/qtscripttoolsversion.h
/usr/lib64/cmake/Qt5Script/Qt5ScriptConfig.cmake
/usr/lib64/cmake/Qt5Script/Qt5ScriptConfigVersion.cmake
/usr/lib64/cmake/Qt5ScriptTools/Qt5ScriptToolsConfig.cmake
/usr/lib64/cmake/Qt5ScriptTools/Qt5ScriptToolsConfigVersion.cmake
/usr/lib64/libQt5Script.prl
/usr/lib64/libQt5Script.so
/usr/lib64/libQt5ScriptTools.prl
/usr/lib64/libQt5ScriptTools.so
/usr/lib64/pkgconfig/Qt5Script.pc
/usr/lib64/pkgconfig/Qt5ScriptTools.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_script.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_script_private.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_scripttools.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_scripttools_private.pri

%files extras
%defattr(-,root,root,-)
/usr/lib64/libQt5ScriptTools.so.5
/usr/lib64/libQt5ScriptTools.so.5.11
/usr/lib64/libQt5ScriptTools.so.5.11.1

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Script.so.5
/usr/lib64/libQt5Script.so.5.11
/usr/lib64/libQt5Script.so.5.11.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/qtscript/LICENSE.FDL
/usr/share/doc/qtscript/LICENSE.GPL2
/usr/share/doc/qtscript/LICENSE.GPL3
/usr/share/doc/qtscript/LICENSE.GPL3-EXCEPT
/usr/share/doc/qtscript/LICENSE.LGPL3
/usr/share/doc/qtscript/src_3rdparty_javascriptcore_JavaScriptCore_COPYING.LIB
/usr/share/doc/qtscript/src_3rdparty_javascriptcore_JavaScriptCore_pcre_COPYING
/usr/share/doc/qtscript/tests_benchmarks_script_sunspider_tests_LICENSE.txt
/usr/share/doc/qtscript/tests_benchmarks_script_v8_tests_LICENSE.txt
