Summary:	A KDE panel applet for quick access to Mozilla
Summary(pl.UTF-8):	Aplet panelu KDE do szybkiego dostępu do Mozilli
Name:		mozillaqs
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/mozillaqs/%{name}-%{version}.tar.gz
# Source0-md5:	772386be5dde0e095f919318eb5178a1
URL:		http://mozillaqs.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	qt-devel >= 6:3.1
Requires:	mozilla >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mozilla Quickstarter is an small KDE utility that runs in the
SystemTray and runs a hidden instance of Mozilla. You can execute
navigator or mail program from Mozilla Quickstarter.

%description -l pl.UTF-8
Mozilla Quickstarter to niewielka, działająca w zasobniku systemowym
aplikacja KDE. Uruchamia ona ukrytą instancję Mozilli. Możliwe jest
uruchomienie przeglądarki lub programu pocztowego z poziomu Mozilla
QuickStarter.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/*.desktop \
        $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
