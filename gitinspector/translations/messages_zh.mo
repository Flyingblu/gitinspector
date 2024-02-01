��    4      �  G   \      x     y     �  8   �     �     �  m   �  A   F     �    �  	   �  (   �      �            
   1     <     J  :   Y  2   �     �     �     �     �  	     E   !      g  o   �  9   �  _   2	  h   �	  ?   �	  Q   ;
  Y   �
  ]   �
  A   E  D   �  �   �  1   e  ]   �  &   �  4       Q  �   b       I   /  $   y     �  &   �  .   �  !     "   0  6  S     �     �  3   �     �     �  ?   �  <   $     a  M  h     �     �     �     �                  '      4   '   D   $   l      �      �      �      �   	   �   '   �      !  <   %!  $   b!  0   �!  0   �!  <   �!  9   &"  <   `"  0   �"  <   �"  '   #  �   3#  <   �#  $   �#  )   $  !   B$  
  d$  �   f.     �.  @   
/     K/     d/  $   t/  %   �/     �/  !   �/         '   .      1                                     ,                /      "       )       %      4                             !      &   	   +              
              $          3       2      *          0       -   (   #                        % in comments % of changes (extensions used during statistical analysis are marked) Age Author Below are the number of rows from each author that have survived and are still intact in the current revision Checking how many rows belong to each author (Progress): {0:.0f}% Commits Copyright © 2012-2015 Ejwa Software. All rights reserved.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Adam Waldenberg. Deletions Error processing git repository at "%s". HTML output not yet supported in Hide minor authors Hide rows with minor work Insertions Minor Authors Modified Rows: No commited files with the specified extensions were found No metrics violations were found in the repository Repository statistics for {0} Rows Show minor authors Show rows with minor work Stability Statistical information for the repository '{0}' was gathered on {1}. Text output not yet supported in The authors with the following emails were excluded from the statistics due to the specified exclusion patterns The extensions below were found in the repository history The following authors were excluded from the statistics due to the specified exclusion patterns The following commit revisions were excluded from the statistics due to the specified exclusion patterns The following files are suspiciously big (in order of severity) The following files have an elevated cyclomatic complexity (in order of severity) The following files have an elevated cyclomatic complexity density (in order of severity) The following files were excluded from the statistics due to the specified exclusion patterns The following historical commit information, by author, was found The following history timeline has been gathered from the repository The following responsibilities, by author, were found in the current revision of the repository (comments are excluded from the line count, if possible) The given option argument is not a valid boolean. The output has been generated by {0} {1}. The statistical analysis tool for git repositories. Try `{0} --help' for more information. Unable to determine absolute path of git repository. Usage: {0} [OPTION]... [REPOSITORY]
List information about the repository in REPOSITORY. If no repository is
specified, the current directory is used. If multiple repositories are
given, information will be fetched from the last repository specified.

Mandatory arguments to long options are mandatory for short options too.
Boolean arguments can only be given to long options.
  -f, --file-types=EXTENSIONS    a comma separated list of file extensions to
                                   include when computing statistics. The
                                   default extensions used are:
                                   {1}
                                   Specifying * includes files with no
                                   extension, while ** includes all files
  -F, --format=FORMAT            define in which format output should be
                                   generated; the default format is 'text' and
                                   the available formats are:
                                   {2}
      --grading[=BOOL]           show statistics and information in a way that
                                   is formatted for grading of student
                                   projects; this is the same as supplying the
                                   options -HlmrTw
  -H, --hard[=BOOL]              track rows and look for duplicates harder;
                                   this can be quite slow with big repositories
  -l, --list-file-types[=BOOL]   list all the file extensions available in the
                                   current branch of the repository
  -L, --localize-output[=BOOL]   localize the generated output to the selected
                                   system language if a translation is
                                   available
  -m  --metrics[=BOOL]           include checks for certain metrics during the
                                   analysis of commits
  -r  --responsibilities[=BOOL]  show which files the different authors seem
                                   most responsible for
      --since=DATE               only show statistics for commits more recent
                                   than a specific date
  -T, --timeline[=BOOL]          show commit timeline, including author names
      --until=DATE               only show statistics for commits older than a
                                   specific date
  -w, --weeks[=BOOL]             show all statistical information in weeks
                                   instead of in months
  -x, --exclude=PATTERN          an exclusion pattern describing the file
                                   paths, revisions, revisions with certain
                                   commit messages, author names or author
                                   emails that should be excluded from the
                                   statistics; can be specified multiple times
  -h, --help                     display this help and exit
      --version                  output version information and exit

gitinspector will filter statistics to only include commits that modify,
add or remove one of the specified extensions, see -f or --file-types for
more information.

gitinspector requires that the git executable is available in your PATH.
Report gitinspector bugs to gitinspector@ejwa.se. WARNING: The terminal encoding is not correctly configured. gitinspector might malfunction. The encoding can be configured with the environment variable 'PYTHONIOENCODING'. XML output not yet supported in gitinspector requires at least Python 2.6 to run (version {0} was found). invalid regular expression specified is mostly responsible for specified output format not supported. {0} ({1:.3f} in cyclomatic complexity density) {0} ({1} estimated lines of code) {0} ({1} in cyclomatic complexity) Project-Id-Version: gitinspector 0.5.0dev
Report-Msgid-Bugs-To: gitinspector@ejwa.se
POT-Creation-Date: 2015-10-02 03:35+0200
PO-Revision-Date: 2015-20-23 18:33-0500
Last-Translator: Bill Wang <wangzhijiebill@gmail.com>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 % 的注释 % 的修改 （已标记统计分析过程中使用的插件） 年龄 作者 下面是每位作者在现在的版本中存留下来的行数 正在检查每位作者贡献了多少行 (进度): {0:.0f} 提交 版权所有 © 2012-2014 Ejwa Software. 保留所有权利。
GPLv3的许可证+：GNU GPL版本3或更高版本<http://gnu.org/licenses/gpl.html>。
这是自由软件：您可以自由地更改并重新发布它。
在法律允许的范围内,没有 任何 保证。

撰写： Adam Waldenberg.
翻译： 王之杰 （Bill Wang） 删除 在处理"%s"库时出现问题 HTML文本输出暂不支持 隐藏次要作者 隐藏次要工作 添加 次要作者 修改过的行 未找到符合条件的已提交文件 未在代码库中发现违反指标 关于{0}代码库统计数据 行数 显示次要作者 显示次要行 稳定性 代码库{0}于{1}采集的统计数据 文本输出暂不支持 下列邮箱相关联的作者已经从数据统计中移除 在代码库中找到下列扩展名 下列作者已按规则从数据统计中移除 下列提交已按规则从数据统计中移除 下列文件过大文件有些可疑 (按严重程度排列) 下列文件过度循环性问题 (按严重程度排列) 下列文件度循环性过度密集 (按严重程度排列) 下列文件已按排除规律移除数据统计 在代码库中找到下列提交记录，已按作者分类 在代码库中收集到下列时间轴 在最新的代码库修改中，找到下列分工，按作者分类。 （在计算代码数量时尽可能的排除了批注） 给予的选项不是一个有效的 布尔值 （boolean） 导出结果基于 {0} {1} 生成。 尝试 `{0} --help' 已获得更多信息 无法确定git库的绝对路径 用法：{0} [选项]... [目录] 
在目录列出有关库的信息,如果没有指定目录，那么将使用现目录。如果有多个目录，
将采用指定的最后一个目录

长选项的强制性参数对短选项也适用
布尔参数只能给予长选项
  -f, --file-types=EXTENSIONS    一串逗号分隔的文件类型
                                   用 ＊ 来包含无扩展名的文件
                                   用 ＊＊ 包涵所有文件
                                   这些文件将会被用于计算统计数据.
                                   默认文件类型:
                                   {1}
  -F, --format=FORMAT            指定生成的输出文件的格式；
                                   默认格式是'text' 和
                                   可选格式:
                                   {2}
      --grading[=BOOL]           按照学生成评判项目的格式，
                                   显示统计数据和信息；
                                   等同于 -HlmrTw 选项
  -H, --hard[=BOOL]              记录行数并且寻找重复的内容;
                                   如果数据库较大，这个可能会需要一些时间
  -l, --list-file-types[=BOOL]   列出所有现在的数据库分支的文件格式
  -L, --localize-output[=BOOL]   在翻译版本存在的前提下，将输出结果翻译到系统语言
  -m  --metrics[=BOOL]           在分析提交时，检查特定指标
  -r  --responsibilities[=BOOL]  显示每位作者主要职责
      --since=DATE               只显示从特定时间起的结果
  -T, --timeline[=BOOL]          显示提交时间轴, 包括作者名称
      --until=DATE               只显示特定时间前的结果
  -w, --weeks[=BOOL]             按周来显示统计数据，而非月
  -x, --exclude=PATTERN          按特定格式排除不应该被统计
                                   的文件，作者名字或邮箱;可以按文件名，
                                   作者名，作者邮箱,提交信息，路径和版本。可以重复
  -h, --help                     显示这个帮助信息并退出
      --version                  显示版本信息并退出

gitinspector 会过滤信息并且仅统计那些修改，增加或减少，指定文件类型的提交，
如需详细信息，请参考 -f 或 --file-types 选项

gitinspector 需要 git 可运行文件 在 PATH 中.
错误报告，请寄 gitinspector@ejwa.se.
翻译错误，请寄 wangzhijiebill@gmail.com 警告：命令指示符编码格式有误。gitinspector可能出错。编码格式可以在环境变量的'PYTHONIOENCODING'下修改 XML文本输出暂不支持 gitinspector 要求 Python版本至少2.6 (已找到版本 {0})  无效的正则表达式 主要分工是 不支持设定的输出文件格式 {0} (循环型结构密集度{1: 3f}) {0}（估测代码行数{1}） {0}（代码循环性结构{1}） 