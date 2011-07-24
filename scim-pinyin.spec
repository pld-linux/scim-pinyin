Summary:	Smart Pinyin IMEngine for Smart Common Input Method platform
Name:		scim-pinyin
Version:	0.5.91
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	fb96d3545090d7681ea03edaced4eccb
Patch0:		%{name}-showallkeys.patch
Patch1:		%{name}-save-in-temp.patch
Patch2:		%{name}-fix-load.patch
Patch3:		%{name}-fix-ms-shuangpin.patch
Patch4:		%{name}-gcc43.patch
URL:		http://www.scim-im.org/projects/imengines/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	scim-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gettext
BuildRequires:	gettext-devel
Requires:	scim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simplified Chinese Smart Pinyin IMEngine for SCIM.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/pinyin.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/pinyin-imengine-setup.so
%{_datadir}/scim/pinyin
%{_datadir}/scim/icons/smart-pinyin.png
