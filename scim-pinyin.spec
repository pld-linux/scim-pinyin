# TODO: skim?
Summary:	Smart Pinyin IMEngine for Smart Common Input Method platform
Summary(pl.UTF-8):	Silnik IM Pinyin dla platformy SCIM
Name:		scim-pinyin
Version:	0.5.92
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.xz
# Source0-md5:	53d436a737799e6f7af9a56bf51858b8
Patch0:		%{name}-showallkeys.patch
Patch1:		%{name}-save-in-temp.patch
Patch2:		%{name}-fix-load.patch
Patch3:		%{name}-fix-ms-shuangpin.patch
Patch4:		%{name}-gcc43.patch
URL:		http://www.scim-im.org/projects/imengines/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.2.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	scim >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simplified Chinese Smart Pinyin IMEngine for SCIM.

%description -l pl.UTF-8
Silnik IM Pinyin do wprowadzania znaków chińskich uproszczonych dla
platformy SCIM.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/pinyin.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/pinyin-imengine-setup.so
%{_datadir}/scim/pinyin
%{_datadir}/scim/icons/smart-pinyin.png
