Summary:	Non-interactive CD Player
Summary(pl):	Nieinteraktywny odtwarzacz CD
Name:		cdplayer
Version:	0.0.96
Release:	2
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://www.mat.uni.torun.pl/~witek/%{name}-%{version}.tar.bz2
URL:		http://www.mat.uni.torun.pl/~witek/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveOS:	Linux

%description
cdplayer is simple, non-interactive CD Player for Linux with "Random
Play" option.

%description -l pl
cdplayer to prosty, nieinteraktywny odtwarzacz p³yt kompaktowych z
opcj± losowego odgrywania ¶cie¿ek.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o cdplayer cdplayer.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_mandir}/pl/man1} \
	$RPM_BUILD_ROOT%{_datadir}/cdplayer

install cdplayer $RPM_BUILD_ROOT%{_bindir}/cdplayer
install cdplayer.htm $RPM_BUILD_ROOT%{_datadir}/cdplayer/cdplayer.htm
install cdplayer.1 $RPM_BUILD_ROOT%{_mandir}/man1/cdplayer.1
install pl/cdplayer.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1/cdplayer.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cdplayer
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%dir %{_datadir}/cdplayer
%{_datadir}/cdplayer/cdplayer.htm
