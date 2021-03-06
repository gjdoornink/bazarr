# -*- coding: utf-8 -*-
from datetime import timedelta, datetime
from enzyme.mkv import MKV, VIDEO_TRACK, AUDIO_TRACK, SUBTITLE_TRACK
import io
import os.path
import requests
import unittest
import zipfile


# Test directory
TEST_DIR = os.path.join(os.path.dirname(__file__), os.path.splitext(__file__)[0])


def setUpModule():
    if not os.path.exists(TEST_DIR):
        r = requests.get('http://downloads.sourceforge.net/project/matroska/test_files/matroska_test_w1_1.zip')
        with zipfile.ZipFile(io.BytesIO(r.content), 'r') as f:
            f.extractall(TEST_DIR)


class MKVTestCase(unittest.TestCase):
    def test_test1(self):
        stream = io.open(os.path.join(TEST_DIR, 'test1.mkv'), 'rb')
        mkv = MKV(stream)
        # info
        self.assertTrue(mkv.info.title is None)
        self.assertTrue(mkv.info.duration == timedelta(minutes=1, seconds=27, milliseconds=336))
        self.assertTrue(mkv.info.date_utc == datetime(2010, 8, 21, 7, 23, 3))
        self.assertTrue(mkv.info.muxing_app == 'libebml2 v0.10.0 + libmatroska2 v0.10.1')
        self.assertTrue(mkv.info.writing_app == 'mkclean 0.5.5 ru from libebml v1.0.0 + libmatroska v1.0.0 + mkvmerge v4.1.1 (\'Bouncin\' Back\') built on Jul  3 2010 22:54:08')
        # video track
        self.assertTrue(len(mkv.video_tracks) == 1)
        self.assertTrue(mkv.video_tracks[0].type == VIDEO_TRACK)
        self.assertTrue(mkv.video_tracks[0].number == 1)
        self.assertTrue(mkv.video_tracks[0].name is None)
        self.assertTrue(mkv.video_tracks[0].language == 'und')
        self.assertTrue(mkv.video_tracks[0].enabled == True)
        self.assertTrue(mkv.video_tracks[0].default == True)
        self.assertTrue(mkv.video_tracks[0].forced == False)
        self.assertTrue(mkv.video_tracks[0].lacing == False)
        self.assertTrue(mkv.video_tracks[0].codec_id == 'V_MS/VFW/FOURCC')
        self.assertTrue(mkv.video_tracks[0].codec_name is None)
        self.assertTrue(mkv.video_tracks[0].width == 854)
        self.assertTrue(mkv.video_tracks[0].height == 480)
        self.assertTrue(mkv.video_tracks[0].interlaced == False)
        self.assertTrue(mkv.video_tracks[0].stereo_mode == 0)
        self.assertTrue(mkv.video_tracks[0].crop == {})
        self.assertTrue(mkv.video_tracks[0].display_width is None)
        self.assertTrue(mkv.video_tracks[0].display_height is None)
        self.assertTrue(mkv.video_tracks[0].display_unit is None)
        self.assertTrue(mkv.video_tracks[0].aspect_ratio_type == 0)
        # audio track
        self.assertTrue(len(mkv.audio_tracks) == 1)
        self.assertTrue(mkv.audio_tracks[0].type == AUDIO_TRACK)
        self.assertTrue(mkv.audio_tracks[0].number == 2)
        self.assertTrue(mkv.audio_tracks[0].name is None)
        self.assertTrue(mkv.audio_tracks[0].language == 'und')
        self.assertTrue(mkv.audio_tracks[0].enabled == True)
        self.assertTrue(mkv.audio_tracks[0].default == True)
        self.assertTrue(mkv.audio_tracks[0].forced == False)
        self.assertTrue(mkv.audio_tracks[0].lacing == True)
        self.assertTrue(mkv.audio_tracks[0].codec_id == 'A_MPEG/L3')
        self.assertTrue(mkv.audio_tracks[0].codec_name is None)
        self.assertTrue(mkv.audio_tracks[0].sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].channels == 2)
        self.assertTrue(mkv.audio_tracks[0].output_sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].bit_depth is None)
        # subtitle track
        self.assertTrue(len(mkv.subtitle_tracks) == 0)
        # chapters
        self.assertTrue(len(mkv.chapters) == 0)
        # tags
        self.assertTrue(len(mkv.tags) == 1)
        self.assertTrue(len(mkv.tags[0].simpletags) == 3)
        self.assertTrue(mkv.tags[0].simpletags[0].name == 'TITLE')
        self.assertTrue(mkv.tags[0].simpletags[0].default == True)
        self.assertTrue(mkv.tags[0].simpletags[0].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[0].string == 'Big Buck Bunny - test 1')
        self.assertTrue(mkv.tags[0].simpletags[0].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[1].name == 'DATE_RELEASED')
        self.assertTrue(mkv.tags[0].simpletags[1].default == True)
        self.assertTrue(mkv.tags[0].simpletags[1].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[1].string == '2010')
        self.assertTrue(mkv.tags[0].simpletags[1].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[2].name == 'COMMENT')
        self.assertTrue(mkv.tags[0].simpletags[2].default == True)
        self.assertTrue(mkv.tags[0].simpletags[2].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[2].string == 'Matroska Validation File1, basic MPEG4.2 and MP3 with only SimpleBlock')
        self.assertTrue(mkv.tags[0].simpletags[2].binary is None)

    def test_test2(self):
        stream = io.open(os.path.join(TEST_DIR, 'test2.mkv'), 'rb')
        mkv = MKV(stream)
        # info
        self.assertTrue(mkv.info.title is None)
        self.assertTrue(mkv.info.duration == timedelta(seconds=47, milliseconds=509))
        self.assertTrue(mkv.info.date_utc == datetime(2011, 6, 2, 12, 45, 20))
        self.assertTrue(mkv.info.muxing_app == 'libebml2 v0.21.0 + libmatroska2 v0.22.1')
        self.assertTrue(mkv.info.writing_app == 'mkclean 0.8.3 ru from libebml2 v0.10.0 + libmatroska2 v0.10.1 + mkclean 0.5.5 ru from libebml v1.0.0 + libmatroska v1.0.0 + mkvmerge v4.1.1 (\'Bouncin\' Back\') built on Jul  3 2010 22:54:08')
        # video track
        self.assertTrue(len(mkv.video_tracks) == 1)
        self.assertTrue(mkv.video_tracks[0].type == VIDEO_TRACK)
        self.assertTrue(mkv.video_tracks[0].number == 1)
        self.assertTrue(mkv.video_tracks[0].name is None)
        self.assertTrue(mkv.video_tracks[0].language == 'und')
        self.assertTrue(mkv.video_tracks[0].enabled == True)
        self.assertTrue(mkv.video_tracks[0].default == True)
        self.assertTrue(mkv.video_tracks[0].forced == False)
        self.assertTrue(mkv.video_tracks[0].lacing == False)
        self.assertTrue(mkv.video_tracks[0].codec_id == 'V_MPEG4/ISO/AVC')
        self.assertTrue(mkv.video_tracks[0].codec_name is None)
        self.assertTrue(mkv.video_tracks[0].width == 1024)
        self.assertTrue(mkv.video_tracks[0].height == 576)
        self.assertTrue(mkv.video_tracks[0].interlaced == False)
        self.assertTrue(mkv.video_tracks[0].stereo_mode == 0)
        self.assertTrue(mkv.video_tracks[0].crop == {})
        self.assertTrue(mkv.video_tracks[0].display_width == 1354)
        self.assertTrue(mkv.video_tracks[0].display_height is None)
        self.assertTrue(mkv.video_tracks[0].display_unit is None)
        self.assertTrue(mkv.video_tracks[0].aspect_ratio_type == 0)
        # audio track
        self.assertTrue(len(mkv.audio_tracks) == 1)
        self.assertTrue(mkv.audio_tracks[0].type == AUDIO_TRACK)
        self.assertTrue(mkv.audio_tracks[0].number == 2)
        self.assertTrue(mkv.audio_tracks[0].name is None)
        self.assertTrue(mkv.audio_tracks[0].language == 'und')
        self.assertTrue(mkv.audio_tracks[0].enabled == True)
        self.assertTrue(mkv.audio_tracks[0].default == True)
        self.assertTrue(mkv.audio_tracks[0].forced == False)
        self.assertTrue(mkv.audio_tracks[0].lacing == True)
        self.assertTrue(mkv.audio_tracks[0].codec_id == 'A_AAC')
        self.assertTrue(mkv.audio_tracks[0].codec_name is None)
        self.assertTrue(mkv.audio_tracks[0].sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].channels == 2)
        self.assertTrue(mkv.audio_tracks[0].output_sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].bit_depth is None)
        # subtitle track
        self.assertTrue(len(mkv.subtitle_tracks) == 0)
        # chapters
        self.assertTrue(len(mkv.chapters) == 0)
        # tags
        self.assertTrue(len(mkv.tags) == 1)
        self.assertTrue(len(mkv.tags[0].simpletags) == 3)
        self.assertTrue(mkv.tags[0].simpletags[0].name == 'TITLE')
        self.assertTrue(mkv.tags[0].simpletags[0].default == True)
        self.assertTrue(mkv.tags[0].simpletags[0].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[0].string == 'Elephant Dream - test 2')
        self.assertTrue(mkv.tags[0].simpletags[0].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[1].name == 'DATE_RELEASED')
        self.assertTrue(mkv.tags[0].simpletags[1].default == True)
        self.assertTrue(mkv.tags[0].simpletags[1].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[1].string == '2010')
        self.assertTrue(mkv.tags[0].simpletags[1].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[2].name == 'COMMENT')
        self.assertTrue(mkv.tags[0].simpletags[2].default == True)
        self.assertTrue(mkv.tags[0].simpletags[2].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[2].string == 'Matroska Validation File 2, 100,000 timecode scale, odd aspect ratio, and CRC-32. Codecs are AVC and AAC')
        self.assertTrue(mkv.tags[0].simpletags[2].binary is None)

    def test_test3(self):
        stream = io.open(os.path.join(TEST_DIR, 'test3.mkv'), 'rb')
        mkv = MKV(stream)
        # info
        self.assertTrue(mkv.info.title is None)
        self.assertTrue(mkv.info.duration == timedelta(seconds=49, milliseconds=64))
        self.assertTrue(mkv.info.date_utc == datetime(2010, 8, 21, 21, 43, 25))
        self.assertTrue(mkv.info.muxing_app == 'libebml2 v0.11.0 + libmatroska2 v0.10.1')
        self.assertTrue(mkv.info.writing_app == 'mkclean 0.5.5 ro from libebml v1.0.0 + libmatroska v1.0.0 + mkvmerge v4.1.1 (\'Bouncin\' Back\') built on Jul  3 2010 22:54:08')
        # video track
        self.assertTrue(len(mkv.video_tracks) == 1)
        self.assertTrue(mkv.video_tracks[0].type == VIDEO_TRACK)
        self.assertTrue(mkv.video_tracks[0].number == 1)
        self.assertTrue(mkv.video_tracks[0].name is None)
        self.assertTrue(mkv.video_tracks[0].language == 'und')
        self.assertTrue(mkv.video_tracks[0].enabled == True)
        self.assertTrue(mkv.video_tracks[0].default == True)
        self.assertTrue(mkv.video_tracks[0].forced == False)
        self.assertTrue(mkv.video_tracks[0].lacing == False)
        self.assertTrue(mkv.video_tracks[0].codec_id == 'V_MPEG4/ISO/AVC')
        self.assertTrue(mkv.video_tracks[0].codec_name is None)
        self.assertTrue(mkv.video_tracks[0].width == 1024)
        self.assertTrue(mkv.video_tracks[0].height == 576)
        self.assertTrue(mkv.video_tracks[0].interlaced == False)
        self.assertTrue(mkv.video_tracks[0].stereo_mode == 0)
        self.assertTrue(mkv.video_tracks[0].crop == {})
        self.assertTrue(mkv.video_tracks[0].display_width is None)
        self.assertTrue(mkv.video_tracks[0].display_height is None)
        self.assertTrue(mkv.video_tracks[0].display_unit is None)
        self.assertTrue(mkv.video_tracks[0].aspect_ratio_type == 0)
        # audio track
        self.assertTrue(len(mkv.audio_tracks) == 1)
        self.assertTrue(mkv.audio_tracks[0].type == AUDIO_TRACK)
        self.assertTrue(mkv.audio_tracks[0].number == 2)
        self.assertTrue(mkv.audio_tracks[0].name is None)
        self.assertTrue(mkv.audio_tracks[0].language == 'eng')
        self.assertTrue(mkv.audio_tracks[0].enabled == True)
        self.assertTrue(mkv.audio_tracks[0].default == True)
        self.assertTrue(mkv.audio_tracks[0].forced == False)
        self.assertTrue(mkv.audio_tracks[0].lacing == True)
        self.assertTrue(mkv.audio_tracks[0].codec_id == 'A_MPEG/L3')
        self.assertTrue(mkv.audio_tracks[0].codec_name is None)
        self.assertTrue(mkv.audio_tracks[0].sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].channels == 2)
        self.assertTrue(mkv.audio_tracks[0].output_sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].bit_depth is None)
        # subtitle track
        self.assertTrue(len(mkv.subtitle_tracks) == 0)
        # chapters
        self.assertTrue(len(mkv.chapters) == 0)
        # tags
        self.assertTrue(len(mkv.tags) == 1)
        self.assertTrue(len(mkv.tags[0].simpletags) == 3)
        self.assertTrue(mkv.tags[0].simpletags[0].name == 'TITLE')
        self.assertTrue(mkv.tags[0].simpletags[0].default == True)
        self.assertTrue(mkv.tags[0].simpletags[0].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[0].string == 'Elephant Dream - test 3')
        self.assertTrue(mkv.tags[0].simpletags[0].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[1].name == 'DATE_RELEASED')
        self.assertTrue(mkv.tags[0].simpletags[1].default == True)
        self.assertTrue(mkv.tags[0].simpletags[1].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[1].string == '2010')
        self.assertTrue(mkv.tags[0].simpletags[1].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[2].name == 'COMMENT')
        self.assertTrue(mkv.tags[0].simpletags[2].default == True)
        self.assertTrue(mkv.tags[0].simpletags[2].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[2].string == 'Matroska Validation File 3, header stripping on the video track and no SimpleBlock')
        self.assertTrue(mkv.tags[0].simpletags[2].binary is None)

    def test_test5(self):
        stream = io.open(os.path.join(TEST_DIR, 'test5.mkv'), 'rb')
        mkv = MKV(stream)
        # info
        self.assertTrue(mkv.info.title is None)
        self.assertTrue(mkv.info.duration == timedelta(seconds=46, milliseconds=665))
        self.assertTrue(mkv.info.date_utc == datetime(2010, 8, 21, 18, 6, 43))
        self.assertTrue(mkv.info.muxing_app == 'libebml v1.0.0 + libmatroska v1.0.0')
        self.assertTrue(mkv.info.writing_app == 'mkvmerge v4.0.0 (\'The Stars were mine\') built on Jun  6 2010 16:18:42')
        # video track
        self.assertTrue(len(mkv.video_tracks) == 1)
        self.assertTrue(mkv.video_tracks[0].type == VIDEO_TRACK)
        self.assertTrue(mkv.video_tracks[0].number == 1)
        self.assertTrue(mkv.video_tracks[0].name is None)
        self.assertTrue(mkv.video_tracks[0].language == 'und')
        self.assertTrue(mkv.video_tracks[0].enabled == True)
        self.assertTrue(mkv.video_tracks[0].default == True)
        self.assertTrue(mkv.video_tracks[0].forced == False)
        self.assertTrue(mkv.video_tracks[0].lacing == False)
        self.assertTrue(mkv.video_tracks[0].codec_id == 'V_MPEG4/ISO/AVC')
        self.assertTrue(mkv.video_tracks[0].codec_name is None)
        self.assertTrue(mkv.video_tracks[0].width == 1024)
        self.assertTrue(mkv.video_tracks[0].height == 576)
        self.assertTrue(mkv.video_tracks[0].interlaced == False)
        self.assertTrue(mkv.video_tracks[0].stereo_mode == 0)
        self.assertTrue(mkv.video_tracks[0].crop == {})
        self.assertTrue(mkv.video_tracks[0].display_width == 1024)
        self.assertTrue(mkv.video_tracks[0].display_height == 576)
        self.assertTrue(mkv.video_tracks[0].display_unit is None)
        self.assertTrue(mkv.video_tracks[0].aspect_ratio_type == 0)
        # audio tracks
        self.assertTrue(len(mkv.audio_tracks) == 2)
        self.assertTrue(mkv.audio_tracks[0].type == AUDIO_TRACK)
        self.assertTrue(mkv.audio_tracks[0].number == 2)
        self.assertTrue(mkv.audio_tracks[0].name is None)
        self.assertTrue(mkv.audio_tracks[0].language == 'und')
        self.assertTrue(mkv.audio_tracks[0].enabled == True)
        self.assertTrue(mkv.audio_tracks[0].default == True)
        self.assertTrue(mkv.audio_tracks[0].forced == False)
        self.assertTrue(mkv.audio_tracks[0].lacing == True)
        self.assertTrue(mkv.audio_tracks[0].codec_id == 'A_AAC')
        self.assertTrue(mkv.audio_tracks[0].codec_name is None)
        self.assertTrue(mkv.audio_tracks[0].sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].channels == 2)
        self.assertTrue(mkv.audio_tracks[0].output_sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].bit_depth is None)
        self.assertTrue(mkv.audio_tracks[1].type == AUDIO_TRACK)
        self.assertTrue(mkv.audio_tracks[1].number == 10)
        self.assertTrue(mkv.audio_tracks[1].name == 'Commentary')
        self.assertTrue(mkv.audio_tracks[1].language == 'eng')
        self.assertTrue(mkv.audio_tracks[1].enabled == True)
        self.assertTrue(mkv.audio_tracks[1].default == False)
        self.assertTrue(mkv.audio_tracks[1].forced == False)
        self.assertTrue(mkv.audio_tracks[1].lacing == True)
        self.assertTrue(mkv.audio_tracks[1].codec_id == 'A_AAC')
        self.assertTrue(mkv.audio_tracks[1].codec_name is None)
        self.assertTrue(mkv.audio_tracks[1].sampling_frequency == 22050.0)
        self.assertTrue(mkv.audio_tracks[1].channels == 1)
        self.assertTrue(mkv.audio_tracks[1].output_sampling_frequency == 44100.0)
        self.assertTrue(mkv.audio_tracks[1].bit_depth is None)
        # subtitle track
        self.assertTrue(len(mkv.subtitle_tracks) == 8)
        self.assertTrue(mkv.subtitle_tracks[0].type == SUBTITLE_TRACK)
        self.assertTrue(mkv.subtitle_tracks[0].number == 3)
        self.assertTrue(mkv.subtitle_tracks[0].name is None)
        self.assertTrue(mkv.subtitle_tracks[0].language == 'eng')
        self.assertTrue(mkv.subtitle_tracks[0].enabled == True)
        self.assertTrue(mkv.subtitle_tracks[0].default == True)
        self.assertTrue(mkv.subtitle_tracks[0].forced == False)
        self.assertTrue(mkv.subtitle_tracks[0].lacing == False)
        self.assertTrue(mkv.subtitle_tracks[0].codec_id == 'S_TEXT/UTF8')
        self.assertTrue(mkv.subtitle_tracks[0].codec_name is None)
        self.assertTrue(mkv.subtitle_tracks[1].type == SUBTITLE_TRACK)
        self.assertTrue(mkv.subtitle_tracks[1].number == 4)
        self.assertTrue(mkv.subtitle_tracks[1].name is None)
        self.assertTrue(mkv.subtitle_tracks[1].language == 'hun')
        self.assertTrue(mkv.subtitle_tracks[1].enabled == True)
        self.assertTrue(mkv.subtitle_tracks[1].default == False)
        self.assertTrue(mkv.subtitle_tracks[1].forced == False)
        self.assertTrue(mkv.subtitle_tracks[1].lacing == False)
        self.assertTrue(mkv.subtitle_tracks[1].codec_id == 'S_TEXT/UTF8')
        self.assertTrue(mkv.subtitle_tracks[1].codec_name is None)
        self.assertTrue(mkv.subtitle_tracks[2].type == SUBTITLE_TRACK)
        self.assertTrue(mkv.subtitle_tracks[2].number == 5)
        self.assertTrue(mkv.subtitle_tracks[2].name is None)
        self.assertTrue(mkv.subtitle_tracks[2].language == 'ger')
        self.assertTrue(mkv.subtitle_tracks[2].enabled == True)
        self.assertTrue(mkv.subtitle_tracks[2].default == False)
        self.assertTrue(mkv.subtitle_tracks[2].forced == False)
        self.assertTrue(mkv.subtitle_tracks[2].lacing == False)
        self.assertTrue(mkv.subtitle_tracks[2].codec_id == 'S_TEXT/UTF8')
        self.assertTrue(mkv.subtitle_tracks[2].codec_name is None)
        self.assertTrue(mkv.subtitle_tracks[3].type == SUBTITLE_TRACK)
        self.assertTrue(mkv.subtitle_tracks[3].number == 6)
        self.assertTrue(mkv.subtitle_tracks[3].name is None)
        self.assertTrue(mkv.subtitle_tracks[3].language == 'fre')
        self.assertTrue(mkv.subtitle_tracks[3].enabled == True)
        self.assertTrue(mkv.subtitle_tracks[3].default == False)
        self.assertTrue(mkv.subtitle_tracks[3].forced == False)
        self.assertTrue(mkv.subtitle_tracks[3].lacing == False)
        self.assertTrue(mkv.subtitle_tracks[3].codec_id == 'S_TEXT/UTF8')
        self.assertTrue(mkv.subtitle_tracks[3].codec_name is None)
        self.assertTrue(mkv.subtitle_tracks[4].type == SUBTITLE_TRACK)
        self.assertTrue(mkv.subtitle_tracks[4].number == 8)
        self.assertTrue(mkv.subtitle_tracks[4].name is None)
        self.assertTrue(mkv.subtitle_tracks[4].language == 'spa')
        self.assertTrue(mkv.subtitle_tracks[4].enabled == True)
        self.assertTrue(mkv.subtitle_tracks[4].default == False)
        self.assertTrue(mkv.subtitle_tracks[4].forced == False)
        self.assertTrue(mkv.subtitle_tracks[4].lacing == False)
        self.assertTrue(mkv.subtitle_tracks[4].codec_id == 'S_TEXT/UTF8')
        self.assertTrue(mkv.subtitle_tracks[4].codec_name is None)
        self.assertTrue(mkv.subtitle_tracks[5].type == SUBTITLE_TRACK)
        self.assertTrue(mkv.subtitle_tracks[5].number == 9)
        self.assertTrue(mkv.subtitle_tracks[5].name is None)
        self.assertTrue(mkv.subtitle_tracks[5].language == 'ita')
        self.assertTrue(mkv.subtitle_tracks[5].enabled == True)
        self.assertTrue(mkv.subtitle_tracks[5].default == False)
        self.assertTrue(mkv.subtitle_tracks[5].forced == False)
        self.assertTrue(mkv.subtitle_tracks[5].lacing == False)
        self.assertTrue(mkv.subtitle_tracks[5].codec_id == 'S_TEXT/UTF8')
        self.assertTrue(mkv.subtitle_tracks[5].codec_name is None)
        self.assertTrue(mkv.subtitle_tracks[6].type == SUBTITLE_TRACK)
        self.assertTrue(mkv.subtitle_tracks[6].number == 11)
        self.assertTrue(mkv.subtitle_tracks[6].name is None)
        self.assertTrue(mkv.subtitle_tracks[6].language == 'jpn')
        self.assertTrue(mkv.subtitle_tracks[6].enabled == True)
        self.assertTrue(mkv.subtitle_tracks[6].default == False)
        self.assertTrue(mkv.subtitle_tracks[6].forced == False)
        self.assertTrue(mkv.subtitle_tracks[6].lacing == False)
        self.assertTrue(mkv.subtitle_tracks[6].codec_id == 'S_TEXT/UTF8')
        self.assertTrue(mkv.subtitle_tracks[6].codec_name is None)
        self.assertTrue(mkv.subtitle_tracks[7].type == SUBTITLE_TRACK)
        self.assertTrue(mkv.subtitle_tracks[7].number == 7)
        self.assertTrue(mkv.subtitle_tracks[7].name is None)
        self.assertTrue(mkv.subtitle_tracks[7].language == 'und')
        self.assertTrue(mkv.subtitle_tracks[7].enabled == True)
        self.assertTrue(mkv.subtitle_tracks[7].default == False)
        self.assertTrue(mkv.subtitle_tracks[7].forced == False)
        self.assertTrue(mkv.subtitle_tracks[7].lacing == False)
        self.assertTrue(mkv.subtitle_tracks[7].codec_id == 'S_TEXT/UTF8')
        self.assertTrue(mkv.subtitle_tracks[7].codec_name is None)
        # chapters
        self.assertTrue(len(mkv.chapters) == 0)
        # tags
        self.assertTrue(len(mkv.tags) == 1)
        self.assertTrue(len(mkv.tags[0].simpletags) == 3)
        self.assertTrue(mkv.tags[0].simpletags[0].name == 'TITLE')
        self.assertTrue(mkv.tags[0].simpletags[0].default == True)
        self.assertTrue(mkv.tags[0].simpletags[0].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[0].string == 'Big Buck Bunny - test 8')
        self.assertTrue(mkv.tags[0].simpletags[0].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[1].name == 'DATE_RELEASED')
        self.assertTrue(mkv.tags[0].simpletags[1].default == True)
        self.assertTrue(mkv.tags[0].simpletags[1].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[1].string == '2010')
        self.assertTrue(mkv.tags[0].simpletags[1].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[2].name == 'COMMENT')
        self.assertTrue(mkv.tags[0].simpletags[2].default == True)
        self.assertTrue(mkv.tags[0].simpletags[2].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[2].string == 'Matroska Validation File 8, secondary audio commentary track, misc subtitle tracks')
        self.assertTrue(mkv.tags[0].simpletags[2].binary is None)

    def test_test6(self):
        stream = io.open(os.path.join(TEST_DIR, 'test6.mkv'), 'rb')
        mkv = MKV(stream)
        # info
        self.assertTrue(mkv.info.title is None)
        self.assertTrue(mkv.info.duration == timedelta(seconds=87, milliseconds=336))
        self.assertTrue(mkv.info.date_utc == datetime(2010, 8, 21, 16, 31, 55))
        self.assertTrue(mkv.info.muxing_app == 'libebml2 v0.10.1 + libmatroska2 v0.10.1')
        self.assertTrue(mkv.info.writing_app == 'mkclean 0.5.5 r from libebml v1.0.0 + libmatroska v1.0.0 + mkvmerge v4.0.0 (\'The Stars were mine\') built on Jun  6 2010 16:18:42')
        # video track
        self.assertTrue(len(mkv.video_tracks) == 1)
        self.assertTrue(mkv.video_tracks[0].type == VIDEO_TRACK)
        self.assertTrue(mkv.video_tracks[0].number == 1)
        self.assertTrue(mkv.video_tracks[0].name is None)
        self.assertTrue(mkv.video_tracks[0].language == 'und')
        self.assertTrue(mkv.video_tracks[0].enabled == True)
        self.assertTrue(mkv.video_tracks[0].default == False)
        self.assertTrue(mkv.video_tracks[0].forced == False)
        self.assertTrue(mkv.video_tracks[0].lacing == False)
        self.assertTrue(mkv.video_tracks[0].codec_id == 'V_MS/VFW/FOURCC')
        self.assertTrue(mkv.video_tracks[0].codec_name is None)
        self.assertTrue(mkv.video_tracks[0].width == 854)
        self.assertTrue(mkv.video_tracks[0].height == 480)
        self.assertTrue(mkv.video_tracks[0].interlaced == False)
        self.assertTrue(mkv.video_tracks[0].stereo_mode == 0)
        self.assertTrue(mkv.video_tracks[0].crop == {})
        self.assertTrue(mkv.video_tracks[0].display_width is None)
        self.assertTrue(mkv.video_tracks[0].display_height is None)
        self.assertTrue(mkv.video_tracks[0].display_unit is None)
        self.assertTrue(mkv.video_tracks[0].aspect_ratio_type == 0)
        # audio track
        self.assertTrue(len(mkv.audio_tracks) == 1)
        self.assertTrue(mkv.audio_tracks[0].type == AUDIO_TRACK)
        self.assertTrue(mkv.audio_tracks[0].number == 2)
        self.assertTrue(mkv.audio_tracks[0].name is None)
        self.assertTrue(mkv.audio_tracks[0].language == 'und')
        self.assertTrue(mkv.audio_tracks[0].enabled == True)
        self.assertTrue(mkv.audio_tracks[0].default == False)
        self.assertTrue(mkv.audio_tracks[0].forced == False)
        self.assertTrue(mkv.audio_tracks[0].lacing == True)
        self.assertTrue(mkv.audio_tracks[0].codec_id == 'A_MPEG/L3')
        self.assertTrue(mkv.audio_tracks[0].codec_name is None)
        self.assertTrue(mkv.audio_tracks[0].sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].channels == 2)
        self.assertTrue(mkv.audio_tracks[0].output_sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].bit_depth is None)
        # subtitle track
        self.assertTrue(len(mkv.subtitle_tracks) == 0)
        # chapters
        self.assertTrue(len(mkv.chapters) == 0)
        # tags
        self.assertTrue(len(mkv.tags) == 1)
        self.assertTrue(len(mkv.tags[0].simpletags) == 3)
        self.assertTrue(mkv.tags[0].simpletags[0].name == 'TITLE')
        self.assertTrue(mkv.tags[0].simpletags[0].default == True)
        self.assertTrue(mkv.tags[0].simpletags[0].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[0].string == 'Big Buck Bunny - test 6')
        self.assertTrue(mkv.tags[0].simpletags[0].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[1].name == 'DATE_RELEASED')
        self.assertTrue(mkv.tags[0].simpletags[1].default == True)
        self.assertTrue(mkv.tags[0].simpletags[1].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[1].string == '2010')
        self.assertTrue(mkv.tags[0].simpletags[1].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[2].name == 'COMMENT')
        self.assertTrue(mkv.tags[0].simpletags[2].default == True)
        self.assertTrue(mkv.tags[0].simpletags[2].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[2].string == 'Matroska Validation File 6, random length to code the size of Clusters and Blocks, no Cues for seeking')
        self.assertTrue(mkv.tags[0].simpletags[2].binary is None)

    def test_test7(self):
        stream = io.open(os.path.join(TEST_DIR, 'test7.mkv'), 'rb')
        mkv = MKV(stream)
        # info
        self.assertTrue(mkv.info.title is None)
        self.assertTrue(mkv.info.duration == timedelta(seconds=37, milliseconds=43))
        self.assertTrue(mkv.info.date_utc == datetime(2010, 8, 21, 17, 0, 23))
        self.assertTrue(mkv.info.muxing_app == 'libebml2 v0.10.1 + libmatroska2 v0.10.1')
        self.assertTrue(mkv.info.writing_app == 'mkclean 0.5.5 r from libebml v1.0.0 + libmatroska v1.0.0 + mkvmerge v4.0.0 (\'The Stars were mine\') built on Jun  6 2010 16:18:42')
        # video track
        self.assertTrue(len(mkv.video_tracks) == 1)
        self.assertTrue(mkv.video_tracks[0].type == VIDEO_TRACK)
        self.assertTrue(mkv.video_tracks[0].number == 1)
        self.assertTrue(mkv.video_tracks[0].name is None)
        self.assertTrue(mkv.video_tracks[0].language == 'und')
        self.assertTrue(mkv.video_tracks[0].enabled == True)
        self.assertTrue(mkv.video_tracks[0].default == False)
        self.assertTrue(mkv.video_tracks[0].forced == False)
        self.assertTrue(mkv.video_tracks[0].lacing == False)
        self.assertTrue(mkv.video_tracks[0].codec_id == 'V_MPEG4/ISO/AVC')
        self.assertTrue(mkv.video_tracks[0].codec_name is None)
        self.assertTrue(mkv.video_tracks[0].width == 1024)
        self.assertTrue(mkv.video_tracks[0].height == 576)
        self.assertTrue(mkv.video_tracks[0].interlaced == False)
        self.assertTrue(mkv.video_tracks[0].stereo_mode == 0)
        self.assertTrue(mkv.video_tracks[0].crop == {})
        self.assertTrue(mkv.video_tracks[0].display_width is None)
        self.assertTrue(mkv.video_tracks[0].display_height is None)
        self.assertTrue(mkv.video_tracks[0].display_unit is None)
        self.assertTrue(mkv.video_tracks[0].aspect_ratio_type == 0)
        # audio track
        self.assertTrue(len(mkv.audio_tracks) == 1)
        self.assertTrue(mkv.audio_tracks[0].type == AUDIO_TRACK)
        self.assertTrue(mkv.audio_tracks[0].number == 2)
        self.assertTrue(mkv.audio_tracks[0].name is None)
        self.assertTrue(mkv.audio_tracks[0].language == 'und')
        self.assertTrue(mkv.audio_tracks[0].enabled == True)
        self.assertTrue(mkv.audio_tracks[0].default == False)
        self.assertTrue(mkv.audio_tracks[0].forced == False)
        self.assertTrue(mkv.audio_tracks[0].lacing == True)
        self.assertTrue(mkv.audio_tracks[0].codec_id == 'A_AAC')
        self.assertTrue(mkv.audio_tracks[0].codec_name is None)
        self.assertTrue(mkv.audio_tracks[0].sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].channels == 2)
        self.assertTrue(mkv.audio_tracks[0].output_sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].bit_depth is None)
        # subtitle track
        self.assertTrue(len(mkv.subtitle_tracks) == 0)
        # chapters
        self.assertTrue(len(mkv.chapters) == 0)
        # tags
        self.assertTrue(len(mkv.tags) == 1)
        self.assertTrue(len(mkv.tags[0].simpletags) == 3)
        self.assertTrue(mkv.tags[0].simpletags[0].name == 'TITLE')
        self.assertTrue(mkv.tags[0].simpletags[0].default == True)
        self.assertTrue(mkv.tags[0].simpletags[0].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[0].string == 'Big Buck Bunny - test 7')
        self.assertTrue(mkv.tags[0].simpletags[0].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[1].name == 'DATE_RELEASED')
        self.assertTrue(mkv.tags[0].simpletags[1].default == True)
        self.assertTrue(mkv.tags[0].simpletags[1].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[1].string == '2010')
        self.assertTrue(mkv.tags[0].simpletags[1].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[2].name == 'COMMENT')
        self.assertTrue(mkv.tags[0].simpletags[2].default == True)
        self.assertTrue(mkv.tags[0].simpletags[2].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[2].string == 'Matroska Validation File 7, junk elements are present at the beggining or end of clusters, the parser should skip it. There is also a damaged element at 451418')
        self.assertTrue(mkv.tags[0].simpletags[2].binary is None)

    def test_test8(self):
        stream = io.open(os.path.join(TEST_DIR, 'test8.mkv'), 'rb')
        mkv = MKV(stream)
        # info
        self.assertTrue(mkv.info.title is None)
        self.assertTrue(mkv.info.duration == timedelta(seconds=47, milliseconds=341))
        self.assertTrue(mkv.info.date_utc == datetime(2010, 8, 21, 17, 22, 14))
        self.assertTrue(mkv.info.muxing_app == 'libebml2 v0.10.1 + libmatroska2 v0.10.1')
        self.assertTrue(mkv.info.writing_app == 'mkclean 0.5.5 r from libebml v1.0.0 + libmatroska v1.0.0 + mkvmerge v4.0.0 (\'The Stars were mine\') built on Jun  6 2010 16:18:42')
        # video track
        self.assertTrue(len(mkv.video_tracks) == 1)
        self.assertTrue(mkv.video_tracks[0].type == VIDEO_TRACK)
        self.assertTrue(mkv.video_tracks[0].number == 1)
        self.assertTrue(mkv.video_tracks[0].name is None)
        self.assertTrue(mkv.video_tracks[0].language == 'und')
        self.assertTrue(mkv.video_tracks[0].enabled == True)
        self.assertTrue(mkv.video_tracks[0].default == False)
        self.assertTrue(mkv.video_tracks[0].forced == False)
        self.assertTrue(mkv.video_tracks[0].lacing == False)
        self.assertTrue(mkv.video_tracks[0].codec_id == 'V_MPEG4/ISO/AVC')
        self.assertTrue(mkv.video_tracks[0].codec_name is None)
        self.assertTrue(mkv.video_tracks[0].width == 1024)
        self.assertTrue(mkv.video_tracks[0].height == 576)
        self.assertTrue(mkv.video_tracks[0].interlaced == False)
        self.assertTrue(mkv.video_tracks[0].stereo_mode == 0)
        self.assertTrue(mkv.video_tracks[0].crop == {})
        self.assertTrue(mkv.video_tracks[0].display_width is None)
        self.assertTrue(mkv.video_tracks[0].display_height is None)
        self.assertTrue(mkv.video_tracks[0].display_unit is None)
        self.assertTrue(mkv.video_tracks[0].aspect_ratio_type == 0)
        # audio track
        self.assertTrue(len(mkv.audio_tracks) == 1)
        self.assertTrue(mkv.audio_tracks[0].type == AUDIO_TRACK)
        self.assertTrue(mkv.audio_tracks[0].number == 2)
        self.assertTrue(mkv.audio_tracks[0].name is None)
        self.assertTrue(mkv.audio_tracks[0].language == 'und')
        self.assertTrue(mkv.audio_tracks[0].enabled == True)
        self.assertTrue(mkv.audio_tracks[0].default == False)
        self.assertTrue(mkv.audio_tracks[0].forced == False)
        self.assertTrue(mkv.audio_tracks[0].lacing == True)
        self.assertTrue(mkv.audio_tracks[0].codec_id == 'A_AAC')
        self.assertTrue(mkv.audio_tracks[0].codec_name is None)
        self.assertTrue(mkv.audio_tracks[0].sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].channels == 2)
        self.assertTrue(mkv.audio_tracks[0].output_sampling_frequency == 48000.0)
        self.assertTrue(mkv.audio_tracks[0].bit_depth is None)
        # subtitle track
        self.assertTrue(len(mkv.subtitle_tracks) == 0)
        # chapters
        self.assertTrue(len(mkv.chapters) == 0)
        # tags
        self.assertTrue(len(mkv.tags) == 1)
        self.assertTrue(len(mkv.tags[0].simpletags) == 3)
        self.assertTrue(mkv.tags[0].simpletags[0].name == 'TITLE')
        self.assertTrue(mkv.tags[0].simpletags[0].default == True)
        self.assertTrue(mkv.tags[0].simpletags[0].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[0].string == 'Big Buck Bunny - test 8')
        self.assertTrue(mkv.tags[0].simpletags[0].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[1].name == 'DATE_RELEASED')
        self.assertTrue(mkv.tags[0].simpletags[1].default == True)
        self.assertTrue(mkv.tags[0].simpletags[1].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[1].string == '2010')
        self.assertTrue(mkv.tags[0].simpletags[1].binary is None)
        self.assertTrue(mkv.tags[0].simpletags[2].name == 'COMMENT')
        self.assertTrue(mkv.tags[0].simpletags[2].default == True)
        self.assertTrue(mkv.tags[0].simpletags[2].language == 'und')
        self.assertTrue(mkv.tags[0].simpletags[2].string == 'Matroska Validation File 8, audio missing between timecodes 6.019s and 6.360s')
        self.assertTrue(mkv.tags[0].simpletags[2].binary is None)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(MKVTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
