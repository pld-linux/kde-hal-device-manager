# TODO:
# - add desktop file
Summary:	kde-hal-device-manager - a port of HAL Device Manager to KDE
Summary(pl):	kde-hal-device-manager - port zarz±dcy urz±dzeñ HAL dla KDE
Name:		kde-hal-device-manager
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://kubuntu.org/~jriddell/kde-hal-device-manager/%{name}_%{version}.tar.gz
# Source0-md5:	6e4f4e042ddf9859e5064a1c55b24d82
URL:		http://www.kde-apps.org/content/show.php?content=33315
Requires:	hal
Requires:	python-PyQt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Port of HAL Device Manager to KDE. Shows what hardware you have on
your system. 

%description -l pl
Port zarz±dcy urz±dzeñ HAL dla KDE. Pokazuje jakie urz±dzenia s± w
systemie.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}
install * $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/*.*
