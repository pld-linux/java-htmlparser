Summary:	HTML Parser - Java library used to parse HTML in either a linear or nested fashion
Summary(pl.UTF-8):	HTML Parser - biblioteka Javy do analizy HTML-a w sposób liniowy lub zagnieżdżony
Name:		htmlparser
Version:	1.6
Release:	0.1
Epoch:		0
License:	LGPL v2.1
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/htmlparser/%{name}1_6_20060610.zip
# Source0-md5:	b51aeabd7db4bc82cff1c489a2e33b77
URL:		http://htmlparser.sourceforge.net/
%if %(locale -a | grep -q '^en_US$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	jdk
BuildRequires:	jpackage-utils >= 1.6
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML Parser is a Java library used to parse HTML in either a linear or
nested fashion. Primarily used for transformation or extraction, it
features filters, visitors, custom tags and easy to use JavaBeans. It
is a fast, robust and well tested package.

%description -l pl.UTF-8
HTML Parser to biblioteka Javy służąca do analizy HTML-a w sposób
liniowy lub zagnieżdżony. Jest używana głównie do transformacji lub
wyciągania danych; zawiera filtry, własne znaczniki i łatwe w użyciu
JavaBeans. Jest szybkim, mającym duże możliwości i dobrze
przetestowanym pakietem.

%package javadoc
Summary:	Javadoc for HTML Parser
Summary(pl.UTF-8):	Dokumentacja Javadoc do biblioteki HTML Parser
Group:		Documentation

%description javadoc
Javadoc for HTML Parser.

%description javadoc -l pl.UTF-8
Dokumentacja Javadoc do biblioteki HTML Parser.

%prep
%setup -q -n %{name}1_6
%{__unzip} -qq src.zip

# third party bundled libs
rm -f lib/sax2.jar
rm -f lib/junit.jar

mv docs/javadoc javadoc

%build
export LC_ALL=en_US # source code not US-ASCII
%ant jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install lib/htmllexer.jar $RPM_BUILD_ROOT%{_javadir}/htmllexer-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s htmllexer-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/htmllexer.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
