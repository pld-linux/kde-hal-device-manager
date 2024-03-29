# TODO:
# - add desktop file
Summary:	kde-hal-device-manager - a port of HAL Device Manager to KDE
Summary(pl.UTF-8):	kde-hal-device-manager - port zarządcy urządzeń HAL dla KDE
Name:		kde-hal-device-manager
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://kubuntu.org/~jriddell/kde-hal-device-manager/%{name}_%{version}.orig.tar.gz
# Source0-md5:	b16811cde547790b6f0f4d9cdfd59fa3
URL:		http://www.kde-apps.org/content/show.php?content=33315
BuildRequires:	python-PyKDE-devel
BuildRequires:	sed >= 4.0
Requires:	hal
Requires:	python-PyQt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Port of HAL Device Manager to KDE. Shows what hardware you have on
your system. 

%description -l pl.UTF-8
Port zarządcy urządzeń HAL dla KDE. Pokazuje jakie urządzenia są w
systemie.

%prep
%setup -q
rm -frd debian
%{__sed} -i 's,Exec=%{name},Exec=%{_libdir}/%{name}/%{name},g' kde-hal-device-manager.desktop

%build
kdepyuic DeviceManagerWidgetUI.ui

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/ \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

mv %{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}
mv %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

install * $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/*.*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
