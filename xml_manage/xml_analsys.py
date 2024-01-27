import xml.etree.ElementTree as ET

# 定义XML数据
xml_data = '''
<Conf>
    <files>
        <logDb>./log/Log.db</logDb>
        <fingerDb>./bin/webfpdiscerner/Finger.dat</fingerDb>
        <confDir>./conf/</confDir>
        <toolBox>./toolbox.dat</toolBox>
        <hotoolBox>./hotool_box.dat</hotoolBox>
    </files>
    <backup ignore_exts=".dll;.onnx;.dylib;.so">
        <item dir="true">batch_web_path_bruter</item>
        <item dir="true">localService</item>
        <item dir="true" ignore_dirs="tesseract">vulnscaner</item>
        <item dir="true" ignore_dirs="tesseract">vulnVerifier</item>
        <item dir="true">web_path_bruter</item>
        <item dir="true">aggregate_searcher</item>
        <item dir="true" ignore_dirs="plugin;pipe_script">cooperative_platform</item>
        <item>http-fuzzer/data/db/fuzz.db</item>
        <item dir="true" ignore_dirs="ProxyBrowser;extensions;lib;log;database/source.level" ignore_files="database/source.sqlite3">http-proxy</item>
        <item app_dir="true">local-bin/search_engines_hack/Bing.json</item>
        <item app_dir="true">local-bin/search_engines_hack/Google.json</item>
        <item app_dir="true">local-bin/search_engines_hack/MoBan.json</item>
        <item app_dir="true">backend_services/bin/proxy_pool/ProxyPool.db</item>
        <item app_dir="true" dir="true" ignore_files="app.xml">backend_services/conf</item>
        <item app_dir="true" dir="true">config</item>
    </backup>
    <proxyPool>
        <localBinPath>./bin/proxy_pool/proxy_pool.exe</localBinPath>
    </proxyPool>
    <server>
        <upgradeAddr>https://tango-api.nosugar.tech/lc8a775f1947175a</upgradeAddr>
    </server>
    <utils>
        <util>
            <individual>false</individual>
            <cname>子域名搜索</cname>
            <group>信息收集工具</group>
            <name>subdomain_searcher</name>
            <path>./bin/subdomain_searcher/subdomain_searcher.exe</path>
            <params>
                <param label="-T">timeout</param>
                <param label="-t">threads</param>
                <param label="-D">delay</param>
                <param label="-data">data</param>
                <param label="-p">proxy</param>
                <param label="-d">domain</param>
                <param label="-c" value="./bin/subdomain_searcher/subdomain_searcher.yaml" isPath="true">config</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>子域名探测</cname>
            <group>信息收集工具</group>
            <name>subdomain_brute</name>
            <path>./bin/subdomain_brute/subdomain_brute.exe</path>
            <params>
                <param label="-T" value="10">timeout</param>
                <param label="-t" value="10">threads</param>
                <param label="-s" value="114.114.114.114">dns_server</param>
                <param label="-D" value="./bin/subdomain_brute/domain.dict" isPath="true">dict</param>
                <param label="-p">proxy</param>
                <param label="-o">output</param>
                <param label="-d">domain</param>
                <param label="-g">get_detail</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>域名信息查询</cname>
            <group>信息收集工具</group>
            <name>dns_search</name>
            <path>./bin/dns_search/dns_search.exe</path>
            <params>
                <param label="-s" value="114.114.114.114">dns_service</param>
                <param label="-p">port</param>
                <param label="-n">net</param>
                <param label="-d">domain</param>
                <param label="-k">keyword</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>Whois信息查询</cname>
            <group>信息收集工具</group>
            <name>whois</name>
            <path>./bin/whois/whois.exe</path>
            <params>
                <param label="-m">mode</param>
                <param label="-c">col</param>
                <param label="-d">domain</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>CDN探测工具</cname>
            <group>信息收集工具</group>
            <name>cdn_finder</name>
            <path>./bin/cdn_find/cdn_find.exe</path>
            <params>
                <param label="-checkdns">checkdns</param>
                <param label="-t">threads</param>
                <param label="-T">timeout</param>
                <param label="-delay">interval</param>
                <param label="-d">domain</param>
                <param label="-m">model</param>
                <param label="-D" value="./bin/cdn_find/dns.txt" isPath="true">dnsPath</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>Web指纹识别</cname>
            <group>信息收集工具</group>
            <name>web_fingerprint_discerner</name>
            <path>./bin/webfpdiscerner/webfpdiscerner.exe</path>
            <params>
                <param label="-match-all">match_all</param>
                <param label="-t">threads</param>
                <param label="-timeout">timeout</param>
                <param label="-s">interval</param>
                <param label="-d">urls</param>
                <param label="-r" isPath="true">urls_file</param>
                <param label="-p">ports</param>
                <param label="-script">script</param>
                <param label="-proxy">proxy</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>端口扫描工具</cname>
            <group>信息收集工具</group>
            <name>port_scan</name>
            <path>./bin/port_scan/port_scan.exe</path>
            <rootPermission>true</rootPermission>
            <params>
                <param label="-d">hosts</param>
                <param label="-f" isPath="true">host_file</param>
                <param label="-m">model</param>
                <param label="-p">ports</param>
                <param label="-proxy">proxy</param>
                <param label="-t">threads</param>
                <param label="-s">interval</param>
                <param label="-nc">network_card</param>
                <param label="-timeout">timeout</param>
                <param label="-times">times</param>
                <param label="-gb">gb</param>
                <param label="-gt">gt</param>
                <param label="-gk">gk</param>
                <param label="-gd">gd</param>
                <param label="-gf">gf</param>
                <param label="-v" value="true">showDetail</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>网站信息探测</cname>
            <group>信息收集工具</group>
            <name>website_previewer</name>
            <path>./bin/web_preview/web_preview.exe</path>
            <params>
                <param label="-d">urls</param>
                <param label="-r" isPath="true">urls_file</param>
                <param label="-p">ports</param>
                <param label="-proxy">proxy</param>
                <param label="-match">reg_str</param>
                <param label="-path">path</param>
                <param label="-add-path">add_path</param>
                <param label="-t">threads</param>
                <param label="-timeout">timeout</param>
                <param label="-s">interval</param>
                <param label="-fr">if_redirect</param>
                <param label="-match-only">match_only</param>
                <param label="-full-data">full_data</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>同IP网站查询</cname>
            <group>信息收集工具</group>
            <name>domain_finder</name>
            <path>./bin/ip_binding_domain_finder/ip_binding_domain_finder.exe</path>
            <params>
                <param label="-D">delay</param>
                <param label="-T">timeout</param>
                <param label="-t">threads</param>
                <param label="-d">domain</param>
                <param label="-g">content</param>
                <param label="-p">proxy</param>
                <param label="-c" value="./bin/ip_binding_domain_finder/ip_binding_domain_finder.yaml" isPath="true">config</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>批量Ping工具</cname>
            <group>信息收集工具</group>
            <name>super_ping</name>
            <path>./bin/super-ping/super-ping.exe</path>
            <params>
                <param label="-f" isPath="true">ip_file</param>
                <param label="-ip">ip</param>
                <param label="-t" value="10">threads</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>SSL证书查看器</cname>
            <group>信息收集工具</group>
            <name>ssl_viewer</name>
            <path>./bin/ssl_viewer/ssl_viewer.exe</path>
            <params>
                <param label="-t">timeout</param>
                <param label="-h">host</param>
                <param label="-proxy">proxy</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>自动化搜索引擎</cname>
            <group>信息收集工具</group>
            <name>search_engines_hack</name>
            <path>../local-bin/search_engines_hack/search_engines_hack.exe</path>
            <atFront>true</atFront>
            <params></params>
        </util>
        <util>
            <individual>true</individual>
            <cname>聚合资产搜索</cname>
            <group>信息收集工具</group>
            <name>aggregate_searcher</name>
            <path>../app/aggregate_searcher/assets/backservice/aggregate_searcher.exe</path>
            <atFrontPath>aggregate_searcher/app.asar</atFrontPath>
            <packageDir>../app/</packageDir>
            <atFront>true</atFront>
            <mountCategory>true</mountCategory>
            <params></params>
        </util>
        <util>
            <individual>false</individual>
            <cname>域传输漏洞检测</cname>
            <group>信息收集工具</group>
            <name>axfr_hunter</name>
            <path>./bin/axfr_hunter/axfr_hunter.exe</path>
            <params>
                <param label="-s" value="114.114.114.114">dns_service</param>
                <param label="-T" value="15">timeout</param>
                <param label="-t" value="10">threads</param>
                <param label="-d">domain</param>
                <param label="-d" isPath="true">domain_file</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>IIS短文件名枚举</cname>
            <group>信息收集工具</group>
            <name>iis_filename_leakage</name>
            <path>./bin/iis_filename_leakage/iis_filename_leakage.exe</path>
            <params>
                <param label="-t">thread_num</param>
                <param label="-D">interval</param>
                <param label="-T">timeout</param>
                <param label="-r">retry_times</param>
                <param label="-proxy">proxy</param>
                <param label="-d">url</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>SVN泄露利用工具</cname>
            <group>信息收集工具</group>
            <name>svn_dumper</name>
            <path>../local-bin/svn_dumper/svn_dumper.exe</path>
            <atFront>true</atFront>
            <params>
                <param label="-url">url</param>
                <param label="-dump">dump</param>
                <param label="-o">output</param>
                <param label="-t">thread</param>
                <param label="-T">timeOut</param>
                <param label="-l">list</param>
                <param label="-la">all_list</param>
                <param label="-r">retry</param>
            </params>
        </util>
        <util>
            <individual>true</individual>
            <cname>漏洞验证工具</cname>
            <group>弱点扫描工具</group>
            <name>vuln_verifier</name>
            <path>../app/vulnVerify/resources/assets/backservice/vulnverify.exe</path>
            <atFrontPath>vulnVerify/resources/app.asar</atFrontPath>
            <packageDir>../app/</packageDir>
            <atFront>true</atFront>
            <remoteServer>true</remoteServer>
            <mountCategory>true</mountCategory>
            <params>
                <param label="-remote">remote</param>
                <param label="-listen">listen</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>综合暴力破解工具</cname>
            <group>弱点扫描工具</group>
            <name>crack_scan</name>
            <path>./bin/go-crack/go-crack.exe</path>
            <params>
                <param label="-i" isPath="true">ip_list</param>
                <param label="-s">server_addr</param>
                <param label="-g">server_type</param>
                <param label="-u" isPath="true">user_dict</param>
                <param label="-p" isPath="true">pass_dict</param>
                <param label="-proxy">proxy</param>
                <param label="-t">timeout</param>
                <param label="-n">threads</param>
            </params>
        </util>
        <util>
            <individual>true</individual>
            <cname>WEB资源探测工具</cname>
            <group>弱点扫描工具</group>
            <name>web_path_bruter</name>
            <path>../app/webPathBruter/static/backend_services/web_path_bruter.exe</path>
            <atFrontPath>webPathBruter/app.asar</atFrontPath>
            <packageDir>../app/</packageDir>
            <atFront>true</atFront>
            <remoteServer>true</remoteServer>
            <mountCategory>true</mountCategory>
            <params></params>
        </util>
        <util>
            <individual>true</individual>
            <cname>WEB资源批量探测工具</cname>
            <group>弱点扫描工具</group>
            <name>batch_web_path_bruter</name>
            <path>../app/batchWebPathBruter/static/backend_services/batch_web_path_bruter.exe</path>
            <atFrontPath>batchWebPathBruter/app.asar</atFrontPath>
            <packageDir>../app/</packageDir>
            <atFront>true</atFront>
            <remoteServer>true</remoteServer>
            <mountCategory>true</mountCategory>
            <params></params>
        </util>
        <util>
            <individual>false</individual>
            <cname>编码加密解密</cname>
            <group>测试辅助工具</group>
            <name>cript</name>
            <path>../local-bin/easy_encoder/easy_encoder.exe</path>
            <atFront>true</atFront>
            <params></params>
        </util>
        <util>
            <individual>false</individual>
            <cname>文本比对工具</cname>
            <group>测试辅助工具</group>
            <name>text_differ</name>
            <path>../local-bin/text_differ/text_differ.exe</path>
            <atFront>true</atFront>
            <params></params>
        </util>
        <util>
            <individual>false</individual>
            <cname>DNS带外工具箱</cname>
            <group>测试辅助工具</group>
            <name>dns_hunter</name>
            <path>http://127.0.0.1:8000</path>
            <outside>true</outside>
            <params></params>
        </util>
        <util>
            <individual>false</individual>
            <cname>正则表达式生成器</cname>
            <group>测试辅助工具</group>
            <name>regexp</name>
            <path>../local-bin/regexp/regexp.exe</path>
            <atFront>true</atFront>
            <params></params>
        </util>
        <util>
            <individual>false</individual>
            <cname>Shell会话管理工具</cname>
            <group>测试辅助工具</group>
            <name>mshell</name>
            <path>./bin/mshell/mshell.exe</path>
            <params>
                <param label="-l">laddr</param>
                <param label="-pip">ip</param>
                <param label="-tp">tp</param>
                <param label="-sa">sa</param>
                <param label="-tk">tk</param>
                <param label="-proxy">proxy</param>
                <param label="-dp">dp</param>
                <param label="-rawudp">rawudp</param>
            </params>
        </util>
        <util>
            <individual>false</individual>
            <cname>代理池服务</cname>
            <group>测试辅助工具</group>
            <name>proxy_pool</name>
            <path>./bin/proxy_pool/proxy_pool.exe</path>
            <params></params>
        </util>
        <util>
            <individual>true</individual>
            <cname>HTTP模糊测试工具</cname>
            <group>漏洞测试工具</group>
            <name>fuzz</name>
            <path>../app/httpFuzz/resources/backgroundService/http_fuzzer.exe</path>
            <atFrontPath>httpFuzz/app.asar</atFrontPath>
            <packageDir>../app/</packageDir>
            <atFront>true</atFront>
            <remoteServer>true</remoteServer>
            <remoteServerAssociated>fuzz_remote</remoteServerAssociated>
            <mountCategory>true</mountCategory>
            <params></params>
        </util>
        <util>
            <individual>true</individual>
            <cname>HTTP模糊测试工具_远端</cname>
            <name>fuzz_remote</name>
            <path>../app/httpFuzz/resources/backgroundService/http_fuzzer.exe</path>
            <packageDir>../app/</packageDir>
            <remoteServer>true</remoteServer>
            <remoteServerAssociated>fuzz</remoteServerAssociated>
            <params>
                <param label="-remote">remote</param>
                <param label="-save">save</param>
                <param label="-listen">listen</param>
            </params>
        </util>
        <util>
            <individual>true</individual>
            <cname>HTTP抓包测试工具</cname>
            <group>漏洞测试工具</group>
            <name>proxy</name>
            <path>../app/httpProxy/resources/static/backgroundService/http_proxy.exe</path>
            <atFrontPath>httpProxy/app.asar</atFrontPath>
            <packageDir>../app/</packageDir>
            <atFront>true</atFront>
            <remoteServer>true</remoteServer>
            <mountCategory>true</mountCategory>
            <params>
                <param label="--check_lib">check_lib</param>
                <param label="--remote">remote</param>
                <param label="--host">host</param>
            </params>
        </util>
        <util>
            <individual>true</individual>
            <cname>协同平台客户端</cname>
            <group>协同作战平台</group>
            <name>cp_client</name>
            <path>../app/cooperativeplatformclient/assets/backservice/client.exe</path>
            <atFrontPath>cooperativeplatformclient/app.asar</atFrontPath>
            <packageDir>../app/</packageDir>
            <atFront>true</atFront>
            <mountCategory>true</mountCategory>
            <params></params>
        </util>
        <util>
            <individual>false</individual>
            <cname>Tanggo后端主程序</cname>
            <name>tanggo_server</name>
            <path>./TangGo-Service.exe</path>
            <params></params>
        </util>
    </utils>
</Conf>'''

root = ET.fromstring(xml_data)

# 遍历每个 <util> 节点，检查 <individual> 和 <atFront> 的值
for util in root.findall('utils/util'):
    individual_value = util.find('individual')
    at_front_value = util.find('atFront')
    remoteServer = util.find('remoteServer')  



    cname_value = util.find('cname').text
    print('cname:', cname_value)
    group_value = util.find('group')
    if group_value is not None:
        group_value = util.find('group').text
        print('group:', group_value)
    else:
        print('group:None')
#    # 检查 <individual>false且<atFront>true 的情况
#    if individual_value.text == 'false' and at_front_value is not None and at_front_value.text == 'true':
#        cname_value = util.find('cname').text
#        print('cname:', cname_value)
#
#    # 检查 <individual>true 且没有 <remoteServer>true 的情况
#    elif individual_value.text == 'true' and remoteServer  is None:
#        cname_value = util.find('cname').text
#        print('cname:', cname_value)

    # 检查 <individual>false且没有<atFront> 的情况
    #if individual_value.text == 'false' and at_front_value is None :
    #    cname_value = util.find('cname').text
    #    print('cname:', cname_value)
#
    ## 检查 <individual>true 且<remoteServer>true的情况
    #elif individual_value.text == 'true' and remoteServer  is not None and remoteServer.text == 'true':
    #    cname_value = util.find('cname').text
    #    print('cname:', cname_value)