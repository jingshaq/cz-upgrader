@startuml
participant "版本管理模块" as VersionManager
participant "下载管理模块" as DownloadManager
participant "版本校验模块" as VerificationManager
participant "备份管理模块" as BackupManager
participant "更新模块" as UpdateManager
participant "回退模块" as RollbackManager

VersionManager -> VersionManager: compareVersions()
alt 新版本高于当前版本
    VersionManager -> DownloadManager: 请求下载新版本
    DownloadManager -> VersionManager: 下载完成
    VersionManager -> VerificationManager: 请求校验新版本
    VerificationManager -> VerificationManager: verifyDownload()
    alt 文件无问题
        VerificationManager -> VersionManager: 校验结果
        VersionManager -> BackupManager: 请求备份当前版本
        BackupManager -> VersionManager: 备份完成
        VersionManager -> UpdateManager: 请求安装新版本
        UpdateManager -> VersionManager: 安装结果