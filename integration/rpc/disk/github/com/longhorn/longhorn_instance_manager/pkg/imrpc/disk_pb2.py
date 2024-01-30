# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/longhorn/longhorn-instance-manager/pkg/imrpc/disk.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgithub.com/longhorn/longhorn-instance-manager/pkg/imrpc/disk.proto\x12\x05imrpc\x1a\x1bgoogle/protobuf/empty.proto\"\xd6\x01\n\x04\x44isk\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x12\n\ntotal_size\x18\x05 \x01(\x03\x12\x11\n\tfree_size\x18\x06 \x01(\x03\x12\x14\n\x0ctotal_blocks\x18\x07 \x01(\x03\x12\x13\n\x0b\x66ree_blocks\x18\x08 \x01(\x03\x12\x12\n\nblock_size\x18\t \x01(\x03\x12\x14\n\x0c\x63luster_size\x18\n \x01(\x03\x12\x0e\n\x06\x64river\x18\x0b \x01(\t\x12\x0c\n\x04name\x18\x0c \x01(\t\"{\n\x0fReplicaInstance\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x11\n\tdisk_name\x18\x03 \x01(\t\x12\x11\n\tdisk_uuid\x18\x04 \x01(\t\x12\x11\n\tspec_size\x18\x05 \x01(\x04\x12\x13\n\x0b\x61\x63tual_size\x18\x06 \x01(\x04\"\x99\x01\n\x11\x44iskCreateRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x11\n\tdisk_uuid\x18\x03 \x01(\t\x12\x11\n\tdisk_path\x18\x04 \x01(\t\x12\x12\n\nblock_size\x18\x05 \x01(\x03\x12\x13\n\x0b\x64isk_driver\x18\x06 \x01(\t\"o\n\x0e\x44iskGetRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x11\n\tdisk_path\x18\x03 \x01(\t\x12\x13\n\x0b\x64isk_driver\x18\x04 \x01(\t\"\x85\x01\n\x11\x44iskDeleteRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x11\n\tdisk_uuid\x18\x03 \x01(\t\x12\x11\n\tdisk_path\x18\x04 \x01(\t\x12\x13\n\x0b\x64isk_driver\x18\x05 \x01(\t\"l\n\x1e\x44iskReplicaInstanceListRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64isk_driver\x18\x03 \x01(\t\"\xcb\x01\n\x1f\x44iskReplicaInstanceListResponse\x12W\n\x11replica_instances\x18\x01 \x03(\x0b\x32<.imrpc.DiskReplicaInstanceListResponse.ReplicaInstancesEntry\x1aO\n\x15ReplicaInstancesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.imrpc.ReplicaInstance:\x02\x38\x01\"\xa0\x01\n DiskReplicaInstanceDeleteRequest\x12\"\n\tdisk_type\x18\x01 \x01(\x0e\x32\x0f.imrpc.DiskType\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x11\n\tdisk_uuid\x18\x03 \x01(\t\x12\x1d\n\x15replcia_instance_name\x18\x04 \x01(\t\x12\x13\n\x0b\x64isk_driver\x18\x05 \x01(\t\"\xab\x01\n\x13\x44iskVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x11\n\tgitCommit\x18\x02 \x01(\t\x12\x11\n\tbuildDate\x18\x03 \x01(\t\x12,\n$instanceManagerDiskServiceAPIVersion\x18\x04 \x01(\x03\x12/\n\'instanceManagerDiskServiceAPIMinVersion\x18\x05 \x01(\x03*%\n\x08\x44iskType\x12\x0e\n\nfilesystem\x10\x00\x12\t\n\x05\x62lock\x10\x01\x32\xbb\x03\n\x0b\x44iskService\x12\x33\n\nDiskCreate\x12\x18.imrpc.DiskCreateRequest\x1a\x0b.imrpc.Disk\x12>\n\nDiskDelete\x12\x18.imrpc.DiskDeleteRequest\x1a\x16.google.protobuf.Empty\x12-\n\x07\x44iskGet\x12\x15.imrpc.DiskGetRequest\x1a\x0b.imrpc.Disk\x12h\n\x17\x44iskReplicaInstanceList\x12%.imrpc.DiskReplicaInstanceListRequest\x1a&.imrpc.DiskReplicaInstanceListResponse\x12\\\n\x19\x44iskReplicaInstanceDelete\x12\'.imrpc.DiskReplicaInstanceDeleteRequest\x1a\x16.google.protobuf.Empty\x12@\n\nVersionGet\x12\x16.google.protobuf.Empty\x1a\x1a.imrpc.DiskVersionResponseB9Z7github.com/longhorn/longhorn-instance-manager/pkg/imrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'github.com.longhorn.longhorn_instance_manager.pkg.imrpc.disk_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/longhorn/longhorn-instance-manager/pkg/imrpc'
  _DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY._options = None
  _DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY._serialized_options = b'8\001'
  _globals['_DISKTYPE']._serialized_start=1506
  _globals['_DISKTYPE']._serialized_end=1543
  _globals['_DISK']._serialized_start=107
  _globals['_DISK']._serialized_end=321
  _globals['_REPLICAINSTANCE']._serialized_start=323
  _globals['_REPLICAINSTANCE']._serialized_end=446
  _globals['_DISKCREATEREQUEST']._serialized_start=449
  _globals['_DISKCREATEREQUEST']._serialized_end=602
  _globals['_DISKGETREQUEST']._serialized_start=604
  _globals['_DISKGETREQUEST']._serialized_end=715
  _globals['_DISKDELETEREQUEST']._serialized_start=718
  _globals['_DISKDELETEREQUEST']._serialized_end=851
  _globals['_DISKREPLICAINSTANCELISTREQUEST']._serialized_start=853
  _globals['_DISKREPLICAINSTANCELISTREQUEST']._serialized_end=961
  _globals['_DISKREPLICAINSTANCELISTRESPONSE']._serialized_start=964
  _globals['_DISKREPLICAINSTANCELISTRESPONSE']._serialized_end=1167
  _globals['_DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY']._serialized_start=1088
  _globals['_DISKREPLICAINSTANCELISTRESPONSE_REPLICAINSTANCESENTRY']._serialized_end=1167
  _globals['_DISKREPLICAINSTANCEDELETEREQUEST']._serialized_start=1170
  _globals['_DISKREPLICAINSTANCEDELETEREQUEST']._serialized_end=1330
  _globals['_DISKVERSIONRESPONSE']._serialized_start=1333
  _globals['_DISKVERSIONRESPONSE']._serialized_end=1504
  _globals['_DISKSERVICE']._serialized_start=1546
  _globals['_DISKSERVICE']._serialized_end=1989
# @@protoc_insertion_point(module_scope)
